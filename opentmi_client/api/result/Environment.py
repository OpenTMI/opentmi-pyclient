from opentmi_client.utils.Base import BaseApi, setter_rules
from opentmi_client.api.result.Framework import Framework

class Environment(BaseApi):
    def __init__(self, framework=None):
        super(Environment, self).__init__()

    @property
    def ref(self):
        return self.get("ref")

    @ref.setter
    @setter_rules()
    def ref(self, value):
        return self.set("ref", value)

    @property
    def framework(self):
        return self.get("framework")

    @framework.setter
    @setter_rules(type=Framework)
    def framework(self, value):
        return self.set("framework", value)