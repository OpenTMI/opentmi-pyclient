import unittest
from mock import MagicMock
from opentmi_client.api import Client
from opentmi_client.transport.transport import Transport

def mock_transport(transport):
    transport.set_token =  MagicMock()
    transport.set_host =  MagicMock()
    transport.get_json = MagicMock()
    transport.post_json = MagicMock()
    transport.put_json = MagicMock()

class TestClient(unittest.TestCase):

    def test_token(self):
        tr_mock = Transport()
        mock_transport(tr_mock)
        client = Client(transport=tr_mock)
        client.set_token('test')
        tr_mock.set_token.assert_called_once_with("test")

    def test_login(self):
        tr_mock = Transport()
        mock_transport(tr_mock)
        client = Client(transport=tr_mock)
        client.login("user", "passwd")
        tr_mock.post_json.assert_called_once_with("http://127.0.0.1:3000/login",
                                                  {"username": "user", "password": "passwd"})

    def test_logout(self):
        tr_mock = Transport()
        mock_transport(tr_mock)
        client = Client(transport=tr_mock)
        client.logout()
        tr_mock.set_token.assert_called_once_with(None)

    def test_version(self):
        client = Client()
        self.assertEqual(client.get_version(), "0.1")

