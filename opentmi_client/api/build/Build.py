"""
OpenTMI module for Test Build
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.build.Ci import Ci
from opentmi_client.api.build.Vcs import Vcs


class Build(BaseApi):
    """
    Build class
    """
    def __init__(self,
                 name=None):
        super(Build, self).__init__()
        if name:
            self.name = name

    @property
    def name(self):
        return self.get("name")

    @name.setter
    @setter_rules()
    def name(self, value):
        self.set("name", value)

    @property
    def type(self):
        return self.get("type")

    @type.setter
    @setter_rules(value_type=str, enum="app lib test")
    def type(self, value):
        self.set("type", value)

    @property
    def ci_tool(self):
        return self.get("ci")

    @ci_tool.setter
    @setter_rules(value_type=Ci)
    def ci_tool(self, value):
        self.set("ci", value)

    @property
    def vcs(self):
        return self.get("vcs")

    @vcs.setter
    @setter_rules(value_type=list, each_type=Vcs)
    def vcs(self, value):
        self.set("vcs", value)

    @property
    def uuid(self):
        return self.get("uuid")

    @name.setter
    @setter_rules()
    def uuid(self, value):
        self.set("uuid", value)

    @property
    def compiled_by(self):
        return self.get("compiledBy")

    @compiled_by.setter
    @setter_rules(enum="CI manual")
    def compiled_by(self, value):
        self.set("compiledBy", value)

    @property
    def change_id(self):
        return self.get("changeId")

    @change_id.setter
    @setter_rules()
    def change_id(self, value):
        self.set("changeId", value)
