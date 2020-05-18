""" OpenTMI module """
# Internal imports
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.testcase import Skip


class Compatible(BaseApi):
    """ Execution class """
    def __init__(self):
        """ Constructor for Execution """
        super().__init__()
