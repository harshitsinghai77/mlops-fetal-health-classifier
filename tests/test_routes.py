from fastapi.testclient import TestClient

from main import app
from utils import load_file

client = TestClient(app)


def test_normal_fetus():
    f_name = "test_data/test_1.json"
    payload = load_file(f_name)

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] == 1
    assert response.json()["prediction_label"] == "Normal"


def test_suspect_fetus():
    f_name = "test_data/test_2.json"
    payload = load_file(f_name)

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] == 2
    assert response.json()["prediction_label"] == "Suspect"


def test_pathological_fetus():
    f_name = "test_data/test_3.json"
    payload = load_file(f_name)

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] == 3
    assert response.json()["prediction_label"] == "Pathological"


def test_invalid_json():
    f_name = "test_data/test_invalid.json"
    payload = load_file(f_name)

    response = client.post("/predict", json=payload)
    assert response.status_code == 404
