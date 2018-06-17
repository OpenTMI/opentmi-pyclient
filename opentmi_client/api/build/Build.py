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
                 name=None,
                 uuid=None,
                 ci_tool=None,
                 vcs=None,
                 type=None):
        super(Build, self).__init__()
        if name:
            self.name = name
        if uuid:
            self.uuid = uuid
        if type:
            self.type = type
        if ci_tool:
            self.ci_tool = ci_tool
        if vcs:
            self.vcs = vcs

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
    @setter_rules(type=str, enum="app lib test")
    def type(self, value):
        self.set("type",  value)

    @property
    def ci_tool(self):
        return self.get("ci")

    @ci_tool.setter
    @setter_rules(type=Ci)
    def ci_tool(self, value):
        self.set("ci", value)

    @property
    def vcs(self):
        return self.get("vcs")

    @vcs.setter
    @setter_rules(type=list, each_type=Vcs)
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
    def compiledBy(self):
        return self.get("compiledBy")

    @compiledBy.setter
    @setter_rules(enum="CI manual")
    def compiledBy(self, value):
        self.set("compiledBy", value)

    @property
    def changeId(self):
        return self.get("changeId")

    @changeId.setter
    @setter_rules()
    def changeId(self, value):
        self.set("changeId", value)
