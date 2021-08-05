from azureml.core.model import Model
from azureml.core import Workspace, Dataset

ws = Workspace.from_config()

model = Model.register(
    workspace=ws,
    model_path="model.joblib",
    model_name="fetal_health_classifier",
    tags={"joblib": "fetal-health-classifier"},
    description="Classify the health of a fetus as Normal, Suspect or Pathological using CTG data",
)

csv_url = "https://www.kaggle.com/andrewmvd/fetal-health-classification/download"
dataset = Dataset.Tabular.from_delimited_files(path=csv_url)
dataset = dataset.register(
    workspace=ws,
    name="fetal_health_dataset_v1",
    description="Dataset containing 2126 records of features extracted from Cardiotocogram exams, which were then classified by three expert obstetritians into 3 classes: Normal Suspect Pathological",
    create_new_version=True,
)

# Get a dataset by name and version number
fetal_health_dataset = Dataset.get_by_name(
    workspace=ws, name="fetal_health_dataset_v1", version=1
)
