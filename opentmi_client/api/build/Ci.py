from opentmi_client.utils.Base import BaseApi, setter_rules


class Location(BaseApi):
    def __init__(self):
        super(Location, self).__init__()

class Ci(BaseApi):

    def __init__(self, system=None, location=None):
        super(Ci, self).__init__()
        if system: self.system = system
        if location: self.location = location

    @property
    def system(self):
        return self.get("system")

    @system.setter
    @setter_rules(type=str, enum="Jenkins travisCI circleCI")
    def system(self, value):
        return self.set("system",  value)

    @property
    def location(self):
        return self.get("location")

    @location.setter
    @setter_rules(type=Location)
    def location(self, value):
        return self.set("location", value)
