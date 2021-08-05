from azureml.core import Workspace, Dataset, Datastore
from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import PipelineData

ws = Workspace.from_config()

# Get a dataset by name and version number
fetal_health_dataset = Dataset.get_by_name(
    workspace=ws, name="Fetal Health Classifier", version=1
)

# bankmarketing_dataset already retrieved with `get_by_name()`
# make it an input to the script step
dataset_input = fetal_health_dataset.as_named_input("input")

# set the output for the pipeline
output = PipelineData(
    "output", datastore=Datastore(ws, "workspaceblobstore"), output_name="output"
)

prep_step = PythonScriptStep(
    script_name="prep.py",
    source_directory="./src",
    arguments=["--input", dataset_input.as_download(), "--output", output],
    inputs=[dataset_input],
    outputs=[output],
    allow_reuse=True,
)