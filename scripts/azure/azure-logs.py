from azureml.core import Workspace
from azureml.core.webservice import Webservice

# requires `config.json` in the current directory
ws = Workspace.from_config()

service = Webservice(ws, "voting-ensemble-deploy")
logs = service.get_logs()

for line in logs.split("\n"):
    print(line)