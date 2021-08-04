#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=harshitsinghai77/mlops-cookbook . 

# List docker images
docker image ls

# Run flask app
docker run -p 127.0.0.1:8000:8000 harshitsinghai77/mlops-cookbook