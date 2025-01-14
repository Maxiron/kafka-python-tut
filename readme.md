# Sample Fintech Transaction Processing System with Kafka Integration

## Overview
This system demonstrates a simple fintech transaction processing system integrated with Apache Kafka. It is designed for efficient handling and processing of transactions.

### Components
- **Kafka Broker**: Handles message queuing and delivery.
- **Zookeeper**: Coordinates Kafka's distributed systems.
- **FastAPI Application**: Provides RESTful API endpoints.
- **Producer**: Sends transactions to Kafka topics.
- **Consumer**: Processes transactions asynchronously.

---

## System Flow

1. **Transaction Submission**:
   - Transactions are submitted via a REST API to the `/transaction` endpoint.

2. **Message Queuing in Kafka**:
   - Producers send transactions as messages to a specified Kafka topic.

3. **Transaction Processing**:
   - Consumers asynchronously process the messages. This step includes running checks and updating the transaction status.

---

## Usage

### Prerequisites
Ensure the following are installed and configured:
- Kafka and Zookeeper
- Python with FastAPI library

### Steps to Run
1. You can build and run the docker compose file to start the containers using:
   ```bash
   docker compose up --build -d
   ```
2. Ensure the `run.sh` script is executable:
   ```bash
   chmod +x run.sh
   ```
3. You can then simulate transactions by running the Python test script:
   ```bash
   python3 test.py
   ```
4. Similarly, you can just run the shell script `run.sh` with the optional `--runtest` argument. This will start the containers and run the test script:
   ```bash
   ./run.sh --runtest
   ```

---

## Notes
- This system provides a basic framework for transaction processing. Additional features like error handling, security, and scaling should be implemented based on production requirements.
- Customize the producer and consumer logic to include specific checks and transaction updates as per your use case.
