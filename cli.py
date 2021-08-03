#!/usr/bin/env python
import click
from model import predict
from utils import check_columns_exists, load_file
from utils.constant import DF_COLUMNS


@click.command()
@click.option(
    "--file_path",
    default="test_data/test_1.json",
    prompt="Classify the health of a fetus as Normal, Suspect or Pathological using Cardiotocograms (CTGs) data",
    help="JSON File path containing features extracted from Cardiotocogram exams",
)
def predictcli(file_path):
    """Predicts fetal_health from cardiotocogram exam based on payload."""

    try:
        payload = load_file(file_path)
        if not check_columns_exists(payload):
            raise TypeError(f"Columns are missing. Expected: {DF_COLUMNS}")
        result = predict(payload)
        prediction_label = result["prediction_label"]
        if prediction_label == "Normal":
            click.echo(click.style(prediction_label, bg="green", fg="white"))
        if prediction_label == "Suspect":
            click.echo(click.style(prediction_label, bg="yellow", fg="white"))
        if prediction_label == "Pathological":
            click.echo(click.style(prediction_label, bg="red", fg="white"))
    except FileNotFoundError:
        print("Invalid file path", file_path)


# scripts/test_3.json

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()
