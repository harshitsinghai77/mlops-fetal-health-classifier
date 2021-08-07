#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=harshitsinghai77/fetal-health-classifier .

# List docker images
docker image ls

# Run FastAPI app
docker run --rm -p 8000:8000 harshitsinghai77/fetal-health-classifier
