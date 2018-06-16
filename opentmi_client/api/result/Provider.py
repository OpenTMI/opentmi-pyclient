from opentmi_client.utils.Base import BaseApi, setter_rules


class Provider(BaseApi):
    def __init__(self, name=None, id=None, ver=None):
        super(Provider, self).__init__()
        if name: self.name = name
        if id: self.id = id
        if ver: self.ver = ver

    @property
    def name(self):
        return self.get("name")

    @name.setter
    @setter_rules()
    def name(self, value):
        return self.set("name", value)

    @property
    def id(self):
        return self.get("id")

    @id.setter
    @setter_rules()
    def id(self, value):
        return self.set("id", value)

    @property
    def ver(self):
        return self.get("ver")

    @ver.setter
    @setter_rules()
    def ver(self, value):
        return self.set("ver", value)

