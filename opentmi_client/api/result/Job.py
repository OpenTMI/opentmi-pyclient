from opentmi_client.utils.Base import BaseApi, setter_rules


class Job(BaseApi):

    def __init__(self, id=None):
        super(Job, self).__init__()
        if id: self.id = id

    @property
    def id(self):
        return self.get("id")

    @id.setter
    @setter_rules()
    def id(self, value):
        return self.set("id", value)