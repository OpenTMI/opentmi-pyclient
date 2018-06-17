"""
OpenTMI Data base class
"""

from json import dumps
from pydash import get, set_, unset, map_values_deep
from inspect import isclass
from opentmi_client.utils import setter_rules, remove_empty_from_dict


class BaseApi(object):
    """
    Base class for Data record
    """
    def __init__(self):
        """
        Constructor for BaseApi
        """
        self.__data = {}

    @property
    def is_empty(self):
        """
        :return: True data is empty
        """
        return len(self.__data.keys()) == 0

    @property
    def data(self):
        """
        Get plain Dictionary object which are suitable for OpenTMI backend
        :return: Dictionary containsi whole data
        """
        data = map_values_deep(self.__data, lambda x: x.data if isinstance(x, BaseApi) else x)
        return remove_empty_from_dict(data)

    def get(self, key, default=None):
        """
        Get value based on key
        :param key: String
        :param default: Default value if not found
        :return: Value for key. Some keys presents another BaseApi object
        """
        return get(self.__data, key, default)

    def set(self, key, value):
        """
        Set value for key
        :param key: String
        :param value: new value for key
        :return: value
        """
        set_(self.__data, key, value)
        return value

    def unset(self, key):
        """
        Remove key from object
        :param key: String
        :return: self
        """
        unset(self.__data, key)
        return self

    def __str__(self):
        """
        Returns stringified json object
        :return: String
        """
        return dumps(self.data, indent=2, default=lambda o: o.data)
