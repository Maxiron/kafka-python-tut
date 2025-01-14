from kafka import KafkaProducer
import json
from datetime import datetime

class TransactionProducer:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )

    async def send_transaction(self, transaction, topic="financial_transactions"):
        try:
            future = self.producer.send(
                topic,
                value=transaction.dict()
            )
            result = await future
            print(f"Transaction sent successfully: {transaction.transaction_id}")
            return {"status": "success", "message": "Transaction sent to processing"}
        except Exception as e:
            print(f"Error sending transaction: {str(e)}")
            return {"status": "error", "message": str(e)}