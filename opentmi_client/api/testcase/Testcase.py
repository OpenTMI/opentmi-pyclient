"""
OpenTMI Testcase module
"""
# Internal imports
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.testcase import *


class Testcase(BaseApi):
    """
    Testcase class
    """
    def __init__(self, tcid):
        """
        Constructor for Testcase
        :param tcid: String
        """
        super()
        self.tcid = tcid
        self.execution = Execution()
        self.other_info = OtherInfo()

    @property
    def tcid(self):
        """
        Getter for test case ID
        :return: String
        """
        return self.get("tcid")

    @tcid.setter
    @setter_rules()
    def tcid(self, value: str):
        """
        Setter for test case ID
        :param value: String
        """
        self.set("tcid", value)

    @property
    def other_info(self):
        """
        Getter for execution
        :return: String
        """
        return self.get("other_info")

    @other_info.setter
    @setter_rules(OtherInfo)
    def other_info(self, value: OtherInfo):
        """
        Setter for other_info
        :param value: OtherInfo
        """
        self.set("other_info", value)

    @property
    def execution(self):
        """
        Getter for execution
        :return: String
        """
        return self.get("execution")

    @execution.setter
    @setter_rules(Execution)
    def execution(self, value: Execution):
        """
        Setter for execution
        :param value: String
        """
        self.set("execution", value)
