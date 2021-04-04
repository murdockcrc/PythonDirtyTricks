# Add compute cluster to workspace
# This cluster won't incurr costs as it will autoscale down to 0 nodes, or up to max 4 nodes

# Define the time interval for autoscaling, in seconds
autoscale_time = 600

from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config()
cpu_cluster_name = "luisdel-cluster"

# Verify that the cluster does not exist already
try:
    cpu_cluster = ComputeTarget(workspace=ws, name=cpu_cluster_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2',
      idle_seconds_before_scaledown=autoscale_time,
      min_nodes=0,
      max_nodes=4)
    cpu_cluster = ComputeTarget.create(ws, cpu_cluster_name, compute_config)

cpu_cluster.wait_for_completion(show_output=True)