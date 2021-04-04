# Create an Azure ML Workspace
from azureml.core import Workspace

workspace_name = 'luisdel-ml'
susbcription_id = '0d42ef99-c937-43f7-8ff1-1e0fd4e5a4b7'
rg_name = 'luisdel'
location = 'westeurope'

ws = Workspace.create(name=workspace_name,
  subscription_id=susbcription_id,
  resource_group=rg_name,
  create_resource_group=True,
  location=location)

# Write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')