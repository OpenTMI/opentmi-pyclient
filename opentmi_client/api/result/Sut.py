"""
OpenTMI SUT (Software under test) module
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class Sut(BaseApi):
    """
    SUT (Software Under Test) class
    """
    @property
    def ref(self):
        """
        Getter for reference
        :return: String
        """
        return self.get("ref")

    @ref.setter
    @setter_rules()
    def ref(self, value):
        """
        Setter for reference
        :param value: String
        """
        self.set("ref", value)

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
