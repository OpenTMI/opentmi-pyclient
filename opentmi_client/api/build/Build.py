#!/usr/bin/env/python

from opentmi_client.utils.Base import BaseApi, setter_rules
from opentmi_client.api.build.Ci import Ci
from opentmi_client.api.build.Vcs import Vcs


class Build(BaseApi):

    def __init__(self,
                 name = None,
                 uuid=None,
                 ci=None,
                 vcs=None,
                 type=None
            ):
        super(Build, self).__init__()
        if name: self.name = name
        if uuid: self.uuid = uuid
        if type: self.type = type
        if ci: self.ci = ci
        if vcs: self.vcs = vcs

    @property
    def name(self):
        return self.get("name")

    @name.setter
    @setter_rules()
    def name(self, value):
        return self.set("name", value)

    @property
    def type(self):
        return self.get("type")

    @type.setter
    @setter_rules(type=str, enum="app lib test")
    def type(self, value):
        return self.set("type",  value)

    @property
    def ci(self):
        return self.get("ci")

    @ci.setter
    @setter_rules(type=Ci)
    def ci(self, value):
        return self.set("ci", value)

    @property
    def vcs(self):
        return self.get("vcs")

    @vcs.setter
    @setter_rules(type=list, each_type=Vcs)
    def vcs(self, value):
        return self.set("vcs", value)

    @property
    def uuid(self):
        return self.get("uuid")

    @name.setter
    @setter_rules()
    def uuid(self, value):
        return self.set("uuid", value)

    @property
    def compiledBy(self):
        return self.get("compiledBy")

    @compiledBy.setter
    @setter_rules(enum="CI manual")
    def compiledBy(self, value):
        return self.set("compiledBy", value)

    @property
    def changeId(self):
        return self.get("changeId")

    @changeId.setter
    @setter_rules()
    def changeId(self, value):
        return self.set("changeId", value)
