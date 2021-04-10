# Add compute cluster to workspace
# This cluster won't incurr costs as it will autoscale down to 0 nodes, or up to max 4 nodes

# Define the time interval for autoscaling, in seconds
autoscale_time = 600

import argparse
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
import os

ws = Workspace.from_config()

# Add arguments to script
parser = argparse.ArgumentParser()
parser.add_argument('--cluster-name', type=str, dest='compute_name', default='compute-cluster', help='Name of the computer cluster')
parser.add_argument('--cluster-nodes-min', type=int, dest='compute_min_nodes', default=0, help='Minimum number of nodes in the cluster. Default: 0')
parser.add_argument('--cluster-nodes-max', type=int, dest='compute_max_nodes', default=4, help='Maximum number of nodes in the cluster. Default: 4')
parser.add_argument('--vm-size', type=str, dest='vm_size', default='STANDARD_D2_V2', help='Size of the VM. Default: \'STANDARD_D2_V2\'')
parser.add_argument('--vm-priority', type=str, dest='vm_priority', default='lowpriority', help='VM priority. Default: low. Possible values: \'dedicated\' or \'lowpriority\'')
args = parser.parse_args()

compute_name = args.compute_name
compute_min_nodes =args.compute_min_nodes
compute_max_nodes = args.compute_max_nodes
vm_size = args.vm_size
vm_priority = args.vm_priority

# Verify that the cluster does not exist already
try:
    cpu_cluster = ComputeTarget(workspace=ws, name=compute_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(
      vm_size=vm_size,
      idle_seconds_before_scaledown=autoscale_time,
      min_nodes=compute_min_nodes,
      max_nodes=compute_max_nodes,
      vm_priority=vm_priority)
    cpu_cluster = ComputeTarget.create(ws, compute_name, compute_config)

cpu_cluster.wait_for_completion(show_output=True)