# Python MLOps

This is an example of a Containerized FastAPI Application the can be the core ingredient in many "recipes", i.e. deploy targets.

### Model deployed in Azure using Azure Machine Learning Studio

```bash
make test_azure_endpoint
```

Endpoint: http://5534d0ff-e421-4bee-bcb1-aa8d66be732d.centralindia.azurecontainer.io/score

Check Makefile for more commands on how to interact with the model.
