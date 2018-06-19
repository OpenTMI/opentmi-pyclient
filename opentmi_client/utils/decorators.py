"""
OpenTMI python client decorators
"""

from enum import Enum
import functools


def setter_rules(type=str, each_type=None, enum=None):
    """
    setter rules
    :param type: required Type
    :param each_type: required type for each items in case of list
    :param enum: String, only allowed items
    :return: decorator function
    :raises: ValueError or TypeError
    example: require int type for setter - otherwise raise ValueError
    @count.setter
    @setter_rules(type=int)
    def count(self, value):
        self.value = value
    """
    def decorator_wrapper(func):
        """
        Decorator wrapper
        :param func: function for wrap
        :return: decorator wrapper
        """
        @functools.wraps(func)
        def function_wrapper(key, value):
            """
            Function wrapper
            :param key:
            :param value: value given for setter
            :return: target function return value
            """
            if not isinstance(value, type):
                raise TypeError("type must be str")
            if each_type:
                if not all(isinstance(i, each_type) for i in value):
                    raise TypeError("{} list values must be {}".format(key, each_type))
            if enum:
                members = Enum("values", enum)
                if value not in members.__members__:
                    raise ValueError("Value {} not in allowed list ({})".format(value, enum))
            return func(key, value)
        return function_wrapper
    return decorator_wrapper
