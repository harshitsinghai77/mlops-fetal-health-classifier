from azureml.core import Workspace
from azureml.core.webservice import Webservice

# requires `config.json` in the current directory
ws = Workspace.from_config()
service = Webservice(ws, "voting-ensemble-deploy")

service.update(enable_app_insights=True)
