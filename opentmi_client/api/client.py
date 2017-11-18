import json
import jsonmerge
import re

# Appliaction modules
from ..utils import is_object_id, get_logger, resolve_host, TransportException
from ..transport import Transport

REQUEST_TIMEOUT = 30

# Generic API to construct Client Object
def create(host='localhost', port=3000, result_converter=None, testcase_converter=None):
    return OpenTmiClient(host, port, result_converter, testcase_converter)


class OpenTmiClient(object):

    __version = 0
    __api = "/api/v"

    def __init__(self,
                 host='localhost',
                 port=3000,
                 result_converter=None,
                 testcase_converter=None,
                 transport=None):
        """
        Constructor for OpenTMI client
        :param host: opentmi host address (default="localhost")
        :param port: opentmi server port (default=3000)
        :param result_converter:
        :param testcase_converter: function
        :param transport: optional Transport layer. Mostly for testing purpose
        """
        self.logger = get_logger()
        self.resultConverter = result_converter
        self._tcConverter = testcase_converter
        self.__transport = Transport(host, port) if not transport else transport

    def login(self, username, password):
        """
        Login to OpenTMI server
        :param username: username for OpenTMI
        :param password: password for OpenTMI
        :return: OpenTmiClient
        """
        payload = {
            "username": username,
            "password": password
        }
        url = self.__transport.host+ "/login"
        response = self.__transport.post_json(url, payload)
        token = response.get("token")
        self.logger.info("Login success. Token: %s", token)
        self.set_token(token)
        return self

    def logout(self):
        self.__transport.set_token(None)
        return self

    def set_token(self, token):
        self.__transport.set_token(token)
        return self

    def get_version(self):
        """get client version number
        """
        return "0.1" # todo


    # Build
    def upload_build(self, build):
        payload = build
        url = self.__resolve_apiuri("/duts/builds")
        try:
            data = self.__transport.post_json(url, payload)
            self.logger.debug("build uploaded successfully")
            return data
        except TransportException as error:
            self.logger.warning("Result upload failed: %s (status: %s)", error.message, error.code)
        except Exception as e:
            self.logger.warning(e)
    # Suite
    def get_suite(self, suite, options=''):
        """get single suite informations
        """
        try:
            campaign_id = self.get_campaign_id(suite)
        except Exception as err:
            self.logger.warning("exception happened while resolving suite: %s" % (suite))
            return None

        if campaign_id is None:
            self.logger.warning("could not resolve campaign id for suite: %s" % (suite))
            return None

        suite = self.__get_suite(campaign_id, options)
        return suite

    # Campaign
    def get_campaign_id(self, campaignName):
        """get campaign id from name
        """
        if is_object_id(campaignName):
            return campaignName

        for c in self.__get_campaigns():
            if c['name'] == campaignName:
                return c['_id']

    def get_campaigns(self):
        return self.__get_campaigns()

    def get_campaign_names(self):
        campaigns = self.__get_campaigns()
        campaign_names = []
        for campaign in campaigns:
            campaign_names.append(campaign['name'])
        return campaign_names

    # Testcase
    def get_testcases(self, filters=''):
        return self.__get_testcases()

    def update_testcase(self, metadata):
        tc = self.__lookup_testcase(metadata['name'])
        if tc:
            self.logger.debug("Update existing TC")
            self.__update_testcase(tc['id'], metadata)
        else:
            self.logger.debug("Create new TC")
            self.__create_testcase(metadata)

    # Result
    def upload_results(self, result):
        """send result to the server
        """
        tc_meta = self._tcConverter(result.tc_metadata) if self._tcConverter else result
        tc = self.__lookup_testcase(tc_meta['tcid'])
        if not tc:
            tc = self.__create_testcase(tc_meta)
            if not tc:
                self.logger.warning("TC creation failed")
                return None

        payload = self.resultConverter(result) if self.resultConverter else result
        url = self.__resolve_apiuri("/results")
        try:
            files = None
            #hasLogs, logFiles = result.hasLogs()
            #if hasLogs:
            #    zipFile = self.__archiveLogs(logFiles)
            #    self.logger.debug(zipFile)
            #    files = {"file": ("logs.zip", open(zipFile), 'rb') }
            #    self.logger.debug(files)
            data = self.__transport.post_json(url, payload, files=files)
            self.logger.debug("result uploaded successfully")
            return data
        except TransportException as error:
            self.logger.warning("result uploaded failed: %s. status_code: %d", error.message, error.code)
        except Exception as e:
            self.logger.warning(e)
        return None

    # Private members

    def __get_testcases(self, filters=''):
        url = self.__resolve_apiuri("/testcases?" + filters)
        return self.__transport.get_json(url)

    def __get_campaigns(self):
        url = self.__resolve_apiuri("/campaigns?f=name")
        return self.__transport.get_json(url)

    def __get_suite(self, suite, options=''):
        url = self.__resolve_apiuri("/campaigns/" + suite + "/suite" + options)
        return  self.__transport.get_json(url)

    def __lookup_testcase(self, tcid):
        url = self.__resolve_apiuri("/testcases?tcid=" + tcid)
        self.logger.debug("Search TC: %s (%s)" % (tcid, url))
        try:
            data = self.__transport.get_json(url)
            if len(data) == 1:
                self.logger.debug("testcase '%s' exists in DB" % tcid)
                return data[0]
        except TransportException as error:
            if error.code == 404:
                self.logger.warning("testcase '%s' not found form DB" % tcid)
            else:
                self.logger.warning("Test case find failed: %s", error.message)
        except Exception as e:
            self.logger.warning(e)

        return None

    def __update_testcase(self, id, metadata):
        url = self.__resolve_apiuri("/testcases/" + id)
        try:
            self.logger.debug("Update TC: %s" % url)
            payload = metadata
            data = self.__transport.put_json(url, payload)
            self.logger.debug("testcase metadata uploaded successfully")
            return data
        except TransportException as error:
            self.logger.debug(error)
        except Exception as e:
            self.logger.debug(e)

        self.logger.warning("testcase metadata upload failed")
        return None

    def __create_testcase(self, metadata):
        url = self.__resolve_apiuri("/testcases")
        try:
            self.logger.debug("Create TC: %s" % url)
            payload = metadata
            data = self.__transport.post_json(url, payload)
            self.logger.debug("new testcase metadata uploaded successfully with id: %s" % json.dumps(data))
            return data
        except TransportException as error:
            self.logger.warning(error)
        except Exception as e:
            self.logger.warning('createTestcase throw exception:')
            self.logger.warning(e)

        self.logger.warning("new testcase metadata upload failed")
        return None

    def __resolve_apiuri(self, path):
        return self.__host + self.__api + str(self.__version) + path
