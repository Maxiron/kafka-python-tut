import uuid
import httpx
import asyncio
import random
from datetime import datetime
from schemas import Transaction, TransactionType

async def simulate_transactions():
    transaction_types = [TransactionType.DEPOSIT, TransactionType.WITHDRAWAL, TransactionType.TRANSFER]
    user_ids = [f"user_{i}" for i in range(1, 6)]
    
    while True:
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            user_id=random.choice(user_ids),
            amount=round(random.uniform(100, 50000), 2),
            transaction_type=random.choice(transaction_types),
            timestamp=datetime.now(),
            description=f"Test transaction at {datetime.now()}"
        )
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8071/transaction",
                json=transaction.dict()
            )
            print(f"Sent transaction: {response.json()}")
        
        await asyncio.sleep(2)  # Wait 2 seconds between transactions

if __name__ == "__main__":
    asyncio.run(simulate_transactions())