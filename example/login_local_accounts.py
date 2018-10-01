import os
from opentmi_client import OpenTmiClient

client = OpenTmiClient(port=3000)
client.login(username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'))
