#!/bin/sh

# Run the docker compose file
docker compose up --build -d


# Optional argument to run the test.py file or not (using --runtest)
if [ "$1" = "--runtest" ]; then

    # Wait for the server to start
    sleep 5
    python3 test.py
fi