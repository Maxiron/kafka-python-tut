from kafka import KafkaConsumer
import json
from threading import Thread
import time

class TransactionConsumer(Thread):
    def __init__(self, bootstrap_servers, topic="financial_transactions"):
        super().__init__()
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')), # Deserialize JSON data
            auto_offset_reset='earliest', # Start reading at the beginning of the topic
            group_id='transaction_processor_group' # Consumer group ID
        )
        self.running = True

    def process_transaction(self, transaction):
        # Simulate transaction processing
        print(f"Processing transaction: {transaction['transaction_id']}")
        time.sleep(1)  # Simulate processing time
        
        # Add your business logic here
        if transaction['amount'] > 10000:
            print(f"Large transaction detected: {transaction['transaction_id']}")
        
        # Update transaction status
        transaction['status'] = 'completed'
        print(f"Transaction completed: {transaction['transaction_id']}")
        print(f"Transaction details: {transaction}")
        return transaction

    def run(self):
        try:
            for message in self.consumer:
                if not self.running:
                    break
                
                transaction = message.value
                processed_transaction = self.process_transaction(transaction)
                
                # Here you could persist the processed transaction to a database
                print(f"Processed transaction: {processed_transaction}")
                
        except Exception as e:
            print(f"Error in consumer: {str(e)}")
        finally:
            self.consumer.close()

    def stop(self):
        self.running = False