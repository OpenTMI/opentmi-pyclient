import unittest
from opentmi_client.transport import Transport
from requests import Response


class TestRequest(unittest.TestCase):

    def test_is_success(self):
        resp = Response()
        resp.status_code = 200
        self.assertTrue(Transport.is_success(resp))
        resp.status_code = 299
        self.assertTrue(Transport.is_success(resp))
        resp.status_code = 300
        self.assertFalse(Transport.is_success(resp))
        resp.status_code = 199
        self.assertFalse(Transport.is_success(resp))

    def test_constructing(self):
        transport = Transport(<)
        transport.set_token('asdf')
