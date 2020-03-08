""" OpenTMI module """
# Internal imports
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class Execution(BaseApi):
    """ Execution class """
    def __init__(self):
        """ Constructor for Execution """
        super()
