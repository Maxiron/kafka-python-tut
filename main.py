# python imports
import uuid
import os

# fastapi imports
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas import Transaction
from producer import TransactionProducer
from consumer import TransactionConsumer


app = FastAPI(title="Fintech Transaction System")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize producer and consumer
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:29092')
producer = TransactionProducer(KAFKA_BOOTSTRAP_SERVERS)
consumer = TransactionConsumer(KAFKA_BOOTSTRAP_SERVERS)

@app.on_event("startup")
async def startup_event():
    # Start the consumer thread
    consumer.start()

@app.on_event("shutdown")
async def shutdown_event():
    # Stop the consumer thread
    consumer.stop()
    consumer.join()


# Define the home route
@app.get("/")
async def home():
    response ={
        "status": True,
        "message": "Kafka server is running"
    }
    # Return a JSON response
    return JSONResponse(content=response)

@app.post("/transaction")
async def create_transaction(transaction: Transaction):
    # Generate transaction ID if not provided
    if not transaction.transaction_id:
        transaction.transaction_id = str(uuid.uuid4())
    
    # Send transaction to Kafka
    result = await producer.send_transaction(transaction)
    
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    
    return {"transaction_id": transaction.transaction_id, "status": "processing"}

@app.get("/transaction/{transaction_id}")
async def get_transaction(transaction_id: str):
    # In a real implementation, you would query your database
    # This is just a placeholder
    return {"message": "Transaction status endpoint"}
