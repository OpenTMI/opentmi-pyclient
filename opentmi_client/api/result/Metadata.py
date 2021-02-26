"""
OpenTMI module for Metadata details
"""
from opentmi_client.utils.Base import BaseApi


class Metadata(BaseApi):
    """
    Environment class
    """
    def __init__(self):
        """
        constructor for Metadata
        """
        super(Metadata, self).__init__()

    def append(self, key: str, value: str):
        """
        Setter for test case keywords
        :param key: String
        :param value: String
        """
        self.set(key, value)
