import unittest
from opentmi_client.transport import Transport
from opentmi_client.utils.exceptions import TransportException
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

    def test_get_json_not_found(self):
        transport = Transport()
        with self.assertRaises(TransportException):
            transport.get_json("localhost")

    def test_get_post_not_found(self):
        transport = Transport()
        with self.assertRaises(TransportException):
            transport.post_json("localhost", {})

    def test_get_put_not_found(self):
        transport = Transport()
        with self.assertRaises(TransportException):
            transport.put_json("localhost", {})
