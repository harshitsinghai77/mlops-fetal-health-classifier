"""CLI commands for ML operations."""
#!/usr/bin/env python
import click
import requests

import model
from utils import load_file


@click.group()
@click.version_option("0.1")
def cli():
    """Machine Learning Utility Belt"""


@cli.command("retrain")
def retrain():
    """Retrain Model
    Retrain the model with the new dataset.
    """

    click.echo(click.style("Retraining Model", bg="green", fg="white"))
    accuracy, model_name = model.retrain()
    click.echo(
        click.style(f"Retrained Model Accuracy: {accuracy}", bg="blue", fg="white")
    )
    click.echo(click.style(f"Retrained Model Name: {model_name}", bg="red", fg="white"))


@cli.command("predict")
@click.option("--file_path", default="test_data/test_1.json", help="file_path")
@click.option("--host", default="http://localhost:8000/predict", help="Host to query")
def mkrequest(file_path, host):
    """Sends prediction to ML Endpoint"""

    click.echo(
        click.style(
            f"Querying host {host} with file: {file_path}", bg="green", fg="white"
        )
    )
    payload = load_file(file_path)
    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"result: {result.text}", fg="white"))


if __name__ == "__main__":
    cli()
