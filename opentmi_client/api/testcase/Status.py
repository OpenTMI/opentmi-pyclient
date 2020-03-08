""" OpenTMI module """
# Internal imports
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class Status(BaseApi):
    """ Status class """
    def __init__(self):
        """ Constructor for Status """
        super()
