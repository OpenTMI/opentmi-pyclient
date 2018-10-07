"""
OpenTMI module for Target
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.build.Hardware import Hardware


class Target(BaseApi):
    """
    Target Class
    """
    def __init__(self):
        super(Target, self).__init__()

    @property
    def type(self):
        """
        Getter for target type
        :return: String
        """
        return self.get("type")

    @type.setter
    @setter_rules(value_type=str, enum="simulate hardware")
    def type(self, value):
        """
        Setter for target type
        :param value: String (simulate/hardware)
        :return: value
        """
        return self.set("type", value)

    @property
    def os(self):
        """
        Getter for target type
        :return: String
        """
        return self.get("os")

    @os.setter
    @setter_rules(value_type=str, enum="win32 win64 unix32 unix64 mbedOS unknown")
    def os(self, value):
        """
        Setter for target os
        :param value: String (win32 win64 unix32 unix64 mbedOS unknown)
        :return: value
        """
        return self.set("os", value)

    @property
    def hw(self):
        """
        Getter for target hw
        :return: Hardware
        """
        return self.get("hw")

    @hw.setter
    @setter_rules(value_type=Hardware)
    def hw(self, value):
        """
        Setter for target hw
        :param value: Hardware
        :return: value
        """
        return self.set("hw", value)
