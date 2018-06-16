from opentmi_client.utils.Base import BaseApi, setter_rules

class Sut(BaseApi):
    def __init__(self):
        super(Sut, self).__init__()

    @property
    def ref(self):
        return self.get("ref")

    @ref.setter
    @setter_rules()
    def ref(self, value):
        return self.set("ref", value)

'''
      gitUrl: {type: String, default: ''},
      buildName: {type: String},
      buildDate: {type: Date},
      buildUrl: {type: String, default: ''},
      buildSha1: {type: String},
      branch: {type: String, default: ''},
      commitId: {type: String, default: ''},
      tag: [{type: String}],
      href: {type: String},
      cut: [{type: String}], // Component Under Test
      fut: [{type: String}] // Feature Under Test
'''