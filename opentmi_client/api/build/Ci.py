"""
OpenTMI module for CI details
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class Location(BaseApi):
    pass


class Ci(BaseApi):
    """
    CI Class
    """
    def __init__(self, system=None, location=None):
        super(Ci, self).__init__()
        if system:
            self.system = system
        if location:
            self.location = location

    @property
    def system(self):
        return self.get("system")

    @system.setter
    @setter_rules(value_type=str, enum="Jenkins travisCI circleCI")
    def system(self, value):
        return self.set("system", value)

    @property
    def location(self):
        return self.get("location")

    @location.setter
    @setter_rules(value_type=Location)
    def location(self, value):
        return self.set("location", value)
