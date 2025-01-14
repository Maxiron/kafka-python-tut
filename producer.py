from kafka import KafkaProducer
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor

class TransactionProducer:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )
        self.executor = ThreadPoolExecutor(max_workers=1)

    async def send_transaction(self, transaction, topic="financial_transactions"):
        try:
            future = self.producer.send(
                topic,
                value=transaction.dict()
            )
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(self.executor, future.get, 10)  # Run the blocking get method in a separate thread
            print(f"Transaction sent successfully: {transaction.transaction_id}")
            return {"status": "success", "message": "Transaction sent to processing"}
        except Exception as e:
            print(f"Error sending transaction: {str(e)}")
            return {"status": "error", "message": str(e)}