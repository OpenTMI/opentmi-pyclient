from opentmi_client.utils.Base import BaseApi, setter_rules


class Framework(BaseApi):

    def __init__(self, name=None, ver=None):
        super(Framework, self).__init__()
        if name: self.name = name
        if ver: self.ver = ver

    @property
    def name(self):
        return self.get("name")

    @name.setter
    @setter_rules()
    def name(self, value):
        return self.set("name", value)

    @property
    def ver(self):
        return self.get("ver")

    @ver.setter
    @setter_rules()
    def ver(self, value):
        return self.set("ver", value)
