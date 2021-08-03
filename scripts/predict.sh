#!/usr/bin/env bash

PORT=8000
echo "Port: $PORT"

# POST for Normal fetal_health
curl -H "Content-Type: application/json" \
    -X POST http://localhost:$PORT/predict \
    -d @../test_data/test_1.json \
    -w '\n'

# POST for Suspect fetal_health
curl -H "Content-Type: application/json" \
    -X POST http://localhost:$PORT/predict \
    -d @../test_data/test_2.json \
    -w '\n'

# POST for Pathological fetal_health
curl -H "Content-Type: application/json" \
    -X POST http://localhost:$PORT/predict \
    -d @../test_data/test_3.json \
    -w '\n'
