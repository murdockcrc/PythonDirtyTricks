from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

experiment_name = 'day1-experiment-hello'
compute_cluster_name = 'luisdel-cluster'
source_directory = './src'
script_file_name = 'hello_world.py'

ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name=experiment_name)

config = ScriptRunConfig(source_directory=source_directory, script=script_file_name, compute_target=compute_cluster_name)

run = experiment.submit(config)
aml_url = run.get_portal_url() # Gets a link to to Azure portal. Follow the experiment progress here
print(aml_url)