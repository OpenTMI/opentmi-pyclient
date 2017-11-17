import json


class Query(object):
    def __init__(self):
        self.__query = {}

    def set(self, key, value):
        self.__query[key] = value
        return self

    def to_string(self):
        return json.dumps(self.__query)


class Request():
    def __init__(self, type):
        self.__request = {
            "t": type,
            "q": Query()}

    @property
    def query(self):
        return self.__request["q"]

    def _set(self, key, value):
        self.__request[key] = value

    def _has(self, key):
        return key in self.__request

    def _push(self, key, value):
        if not self._has(key):
            self._set("f", "")
        else:
            self.__request[key] += " "
        self.__request[key] += value

    def params(self):
        request = self.__request.copy()
        request["q"] = request["q"].to_string()
        return request


class Find(Request):
    def __init__(self):
        Request.__init__(self, "find")

    def limit(self, limit):
        self._set("l", limit)
        return self

    def skip(self, skip):
        self._set("sk", skip)
        return self

    def select(self, field):
        self._push("f", field)
        return self


class Distinct(Request):
    def __init__(self):
        Request.__init__(self, "find")

    def limit(self, limit):
        self._set("l", limit)
        return self

    def skip(self, skip):
        self._set("sk", skip)
        return self

    def select(self, field):
        self._set("f", field)
