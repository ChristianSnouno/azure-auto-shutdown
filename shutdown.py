from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import os

cred = DefaultAzureCredential()
sub_id = os.environ["AZURE_SUBSCRIPTION_ID"]
client = ComputeManagementClient(cred, sub_id)

for vm in client.virtual_machines.list_all():
    tags = vm.tags or {}
    if tags.get("auto-stop", "").lower() != "true":
        continue

    group = vm.id.split("/")[4]
    status = client.virtual_machines.instance_view(group, vm.name).statuses[-1].display_status

    if "running" in status.lower():
        print(f" Stopping VM: {vm.name}")
        client.virtual_machines.begin_power_off(group, vm.name).wait()
        print(f" VM stopped: {vm.name}")
