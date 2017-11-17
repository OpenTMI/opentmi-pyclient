class OpentmiException(Exception):
    def __init__(self, message):
        self.message = message

class TransportException(OpentmiException):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code


