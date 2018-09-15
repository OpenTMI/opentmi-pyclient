"""
OpentTMI module for DUT (Device under test)
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.result.Provider import Provider


class Dut(BaseApi):
    """
    Dut class
    """

    @property
    def count(self):
        return self.get("count")

    @count.setter
    @setter_rules(value_type=int)
    def count(self, value):
        return self.set("count", value)

    @property
    def type(self):
        return self.get("type")

    @type.setter
    @setter_rules(enum="hw simulator process")
    def type(self, value):
        return self.set("type", value)

    @property
    def ref(self):
        return self.get("ref")

    @ref.setter
    @setter_rules()
    def ref(self, value):
        return self.set("ref", value)

    @property
    def vendor(self):
        return self.get("vendor")

    @vendor.setter
    @setter_rules()
    def vendor(self, value):
        return self.set("vendor", value)

    @property
    def model(self):
        return self.get("model")

    @model.setter
    @setter_rules()
    def model(self, value):
        return self.set("model", value)

    @property
    def ver(self):
        return self.get("ver")

    @ver.setter
    @setter_rules()
    def ver(self, value):
        return self.set("ver", value)

    @property
    def sn(self):
        return self.get("sn")

    @sn.setter
    @setter_rules()
    def sn(self, value):
        return self.set("sn", value)

    @property
    def provider(self):
        return self.get("provider")

    @provider.setter
    @setter_rules(value_type=Provider)
    def provider(self, value):
        return self.set("provider", value)
