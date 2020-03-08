""" OpenTMI OtherInfo module """
# Internal imports
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class OtherInfo(BaseApi):
    """ OtherInfo class """
    def __init__(self):
        """ Constructor for OtherInfo """
        super()

    @property
    def title(self):
        """
        Getter for title
        :return: String
        """
        return self.get("title")

    @title.setter
    @setter_rules()
    def title(self, value: str):
        """
        Setter for test case title
        :param value: String
        """
        self.set("title", value)

    @property
    def type(self):
        """
        Getter for type
        :return: String
        """
        return self.get("type")

    @type.setter
    @setter_rules(enum=[
        'installation',
        'compatibility',
        'smoke',
        'regression',
        'acceptance',
        'alpha',
        'beta',
        'stability',
        'functional',
        'destructive',
        'performance',
        'reliability'])
    def type(self, value: str):
        """
        Setter for test case type
        :param value: String
        """
        self.set("type", value)

    @property
    def purpose(self):
        """
        Getter for purpose
        :return: String
        """
        return self.get("purpose")

    @purpose.setter
    @setter_rules()
    def purpose(self, value: str):
        """
        Setter for test case purpose
        :param value: String
        """
        self.set("purpose", value)
