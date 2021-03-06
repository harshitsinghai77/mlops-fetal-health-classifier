import logging

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
import joblib

import model
from utils import check_columns_exists
from utils.constant import DF_COLUMNS

LOGGER = logging.getLogger(__name__)

app = FastAPI()

MODEL_NAME = "model.joblib"
clf = joblib.load(MODEL_NAME)


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h3>Classify the health of a fetus as Normal, Suspect or Pathological using CTG data</h3>"


@app.post("/predict")
async def predict(request: Request):
    """Classify the health of a fetus as Normal, Suspect or Pathological using CTG data"""

    json_payload = await request.json()
    if not check_columns_exists(json_payload):
        raise HTTPException(
            status_code=404, detail=f"Invalid body, expected {DF_COLUMNS}"
        )
    # LOGGER.info(f"JSON payload: {json_payload}")

    payload = model.format_input(json_payload)
    scaled_input_result = model.scale_input(payload)  # scale feature input
    fetal_health_prediction = clf.predict(scaled_input_result)  # scaled prediction
    prediction = model.human_readable_payload(fetal_health_prediction)
    return prediction


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
