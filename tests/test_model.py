import pytest

import pandas as pd
import numpy as np
from click.testing import CliRunner

import utilscli
from cli import predictcli
from model import format_input, scale_input
from utils import load_file


@pytest.fixture
def test_payload():
    f_name = "test_data/test_1.json"
    payload = load_file(f_name)
    return payload


def test_format_input(test_payload):
    test_payload = format_input(test_payload)
    assert isinstance(test_payload, pd.DataFrame)


def test_clisearch():
    runner = CliRunner()
    result = runner.invoke(predictcli, ["--file_path", "test_data/test_1.json"])
    assert result.exit_code == 0
    assert "Normal" in result.output

    result = runner.invoke(predictcli, ["--file_path", "test_data/test_2.json"])
    assert result.exit_code == 0
    assert "Suspect" in result.output

    result = runner.invoke(predictcli, ["--file_path", "test_data/test_3.json"])
    assert result.exit_code == 0
    assert "Pathological" in result.output


def test_retrain():
    runner = CliRunner()
    result = runner.invoke(utilscli.cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1" in result.output
