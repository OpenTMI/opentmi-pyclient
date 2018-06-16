from json import dumps
from pydash import get, set_, unset
from opentmi_client.utils import setter_rules


class BaseApi(object):
    def __init__(self):
        self.__data = {}

    @property
    def empty(self):
        return len(self.data.keys()) == 0

    @property
    def data(self):
        return self.__data

    def get(self, key, default=None):
        return get(self.__data, key, default)

    def set(self, key, value):
        set_(self.__data, key, value)
        return value

    def unset(self, key):
        unset(self.__data, key)
        return self

    def __str__(self):
        return dumps(self.data, indent=2, default=lambda o: o.data)
