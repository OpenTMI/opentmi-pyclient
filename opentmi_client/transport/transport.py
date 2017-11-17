import requests
import json
from requests import request, Response, RequestException
from ..utils import get_logger, resolve_host, TransportException

REQUEST_TIMEOUT = 30
NOT_FOUND = 404


class Transport(object):

    __request_timeout = 10

    def __init__(self, host, port):
        self.logger = get_logger()
        self.__token = None
        self.__host = resolve_host(host, port)
        self.logger.info("OpenTMI host: %s", self.__host)

    def set_token(self, token):
        self.__token = token

    @property
    def __headers(self):
        headers={
            "content-type": "application/json",
            "Connection": "close"
        }
        if self.__token:
            headers["Authorization"] = "Bearer "+self.__token

    def get_json(self, url, params):
        try:
            self.logger.debug("GET: %s" % url)
            response = requests.get(url,
                                    headers=self.__headers,
                                    timeout=REQUEST_TIMEOUT,
                                    params=params)
            if Transport.is_success(response):
                return response.json()
            elif response.status_code == NOT_FOUND:
                self.logger.warning("not found")
        except RequestException as e:
            self.logger.warning("Connection error %s", e.message)
            raise TransportException(e.message)
        except (ValueError, TypeError) as error:
            raise TransportException(error.message)
        return None

    def post_json(self, url, payload, files=[]):
        try:
            response = requests.post(url,
                                     data=json.dumps(payload),
                                     headers=self.__headers,
                                     files=files,
                                     timeout=REQUEST_TIMEOUT)
            if Transport.is_success(response):
                data = json.loads(response.text)
                return data
            else:
                self.logger.warning("status_code: ", response.status_code)
                self.logger.warning(response.text)
                raise TransportException(response.text, response.status_code)
        except RequestException as e:
            self.logger.warning(e)
            raise TransportException(e.message)
        except (JSONDecodeError, TypeError, KeyError) as error:
            raise TransportException(error.message)
        except Exception as e:
            self.logger.warning(e)
            raise TransportException(e.message)

    def put_json(self, url, payload):
        try:
            response = requests.put(url,
                                    data=json.dumps(payload),
                                    headers=self.__headers,
                                    timeout=REQUEST_TIMEOUT)
            if Transport.is_success(response):
                data = json.loads(response.text)
                return data
            else:
                self.logger.warning("status_code: ", response.status_code)
                self.logger.warning(response.text)
                raise TransportException(response.text, response.status_code)
        except RequestException as e:
            self.logger.warning(e)
            raise TransportException(e.message)
        except (JSONDecodeError, TypeError) as error:
            raise TransportException(error.message)
        except Exception as e:
            self.logger.warning(e)
            raise TransportException(e.message)

    @staticmethod
    def is_success(response):
        assert isinstance(response, Response)
        code = response.status_code
        return 300 > code >= 200
