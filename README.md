# Python MLOps

Containerized FastAPI Application to classify the health of a fetus as Normal, Suspect or Pathological using Cardiotocograms CTG data.

## Data

This dataset contains 2126 records of features extracted from Cardiotocogram exams, which were then classified by three expert obstetritians into 3 classes:

Normal
Suspect
Pathological

### Model deployed in Azure using Azure Machine Learning Studio

```bash
make test_azure_endpoint
```

Endpoint: http://5534d0ff-e421-4bee-bcb1-aa8d66be732d.centralindia.azurecontainer.io/score

Check Makefile for more commands on how to interact with the model.

## Azure support

To check the azure scripts go to `scripts/azure` directory.

## GithuAction

The projects has CI support using GitHub Actions.

## ML Inference via command line

```bash
python cli.py
```

Path to the json file containing the test data.

## Model training

Using various classifers to train the dataset and comparing model performance to chose the best model out of all the classifiers.

Find out more `model.py`

The output is the Accuracy, Recall, Precision, F1 Score of the chosen classifier.
Saved the model as `.joblib` and output the name of the saved model along with the accuracy.

## Retrain via command line

```bash
python utilscli.py
```

CLI follows the following commands

1. `--version`
2. `--help`
3. `precit`
4. `retrain`

## FastAPI server

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

Go to http://127.0.0.1:8000/docs

## Test

```bash
make test
```

## Test local endpoints

```bash
make predict
```

## Test prod endpoints

```bash
make test_azure_endpoint
```

## Kubernetes support

```bash
kubectl apply -f kubernetes.yaml
```

## Docker

Build docker images

```bash
make build_docker
```

Run docker container

```bash
make run_docker
```

Lint Docker

```bash
make docker_lint
```
