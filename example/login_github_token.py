import os
from opentmi_client import OpenTmiClient

TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')
client = OpenTmiClient(port=3000)
client.login_with_access_token(access_token=TOKEN)
