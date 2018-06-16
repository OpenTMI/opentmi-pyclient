from enum import Enum
import functools

def setter_rules(type=str, each_type=None, enum=None):
    def decorator_wrapper(func):
        @functools.wraps(func)
        def function_wrapper(key, value):
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