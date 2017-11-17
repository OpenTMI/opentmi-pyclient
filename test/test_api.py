import unittest
from opentmi_client.api.opentmi_client import OpenTmiClient as Client


class TestClient(unittest.TestCase):

    def test_is_success(self):
        resp = Client()
