# pylint: disable=too-many-public-methods
"""
OpenTmiClient module
"""
# standard imports
import os
# 3rd party imports
import deprecation
# Application imports
from opentmi_client.utils import get_logger
from opentmi_client.utils import requires_logged_in
from opentmi_client.utils import OpentmiException, TransportException
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.transport import Transport
from opentmi_client.api.result import Result
from opentmi_client.api.build import Build
from opentmi_client.api.event import Event
from opentmi_client.api.testcase import Testcase
from opentmi_client.api.resource import Resource


REQUEST_TIMEOUT = 30

ENV_GITHUB_ACCESS_TOKEN = "OPENTMI_GITHUB_ACCESS_TOKEN"
ENV_OPENTMI_USERNAME = "OPENTMI_USERNAME"
ENV_OPENTMI_PASSWORD = "OPENTMI_PASSWORD"


# pylint: disable-msg=too-many-arguments
def create(host='localhost', port=None, result_converter=None,
           testcase_converter=None, logger=None):
    """
    Generic create -api for Client
    :param host:
    :param port:
    :param result_converter: optional converter function
    :param testcase_converter: optional converter function
    :param logger: optional logging instance
    :return: OpenTmiClient
    """
    client = OpenTmiClient(host, port, logger)
    client.set_result_converter(result_converter)
    client.set_tc_converter(testcase_converter)
    return client


class OpenTmiClient(object):
    """
    OpenTmiClient object
    """
    __version = 0
    __api = "/api/v"

    # pylint: disable-msg=too-many-arguments
    def __init__(self,
                 host='127.0.0.1',
                 port=None,
                 transport=None,
                 logger=None):
        """
        Constructor for OpenTMI client
        :param host: opentmi host address (default="localhost")
        :param port: opentmi server port (default=3000)
        :param transport: optional Transport layer. Mostly for testing purpose
        :param logger: optional Logging instance.
        """
        self.__logger = logger or get_logger()
        self.__transport = Transport(host, port) if not transport else transport
        # backward compatibility
        self.__result_converter = None
        self.__tc_converter = None
        self.try_login()

    def set_result_converter(self, func):
        """
        Set custom result converter
        :param func: conversion function
        :return: None
        """
        self.__result_converter = func

    def set_tc_converter(self, func):
        """
        Set custom test case converter
        :param func: conversion function
        :return: None
        """
        self.__tc_converter = func

    def login(self, username, password):
        """
        Login to OpenTMI server
        :param username: username for OpenTMI
        :param password: password for OpenTMI
        :return: OpenTmiClient
        """
        payload = {
            "email": username,
            "password": password
        }
        url = self.__resolve_url("/auth/login")
        response = self.__transport.post_json(url, payload)
        token = response.get("token")
        self.logger.info("Login success. Token: %s", token)
        self.set_token(token)
        return self

    def login_with_access_token(self, access_token, service="github"):
        """
        Login to OpenTMI server using access token
        :param access_token: access token to be used
        :param service: access token provider
        :return: OpenTmiClient
        """
        payload = {
            "access_token": access_token
        }
        url = "{}/auth/{}/token".format(self.__transport.host, service)
        self.logger.debug("Login using %s token", service)
        response = self.__transport.post_json(url, payload)
        token = response.get("token")
        self.logger.info("Login success. Token: %s", token)
        self.set_token(token)
        return self

    @property
    def is_logged_in(self):
        """
        get logged in state
        :return: boolean true if logged in.
        """
        return self.__transport.has_token()

    def set_logger(self, logger):
        """
        Set custom logger
        :param logger: logging.Logger instance
        :return: OpenTmiClient
        """
        self.__logger = logger
        return self

    @property
    def logger(self):
        """
        getter for logger
        :return: Logger
        """
        return self.__logger

    def logout(self):
        """
        Logout
        :return: OpenTmiClient
        """
        self.__transport.set_token(None)
        return self

    def set_token(self, token):
        """
        Set authentication token for transport layer
        :param token:
        :return: OpenTmiClient
        """
        self.__transport.set_token(token)
        return self

    def get_version(self):
        """
        Get Client version
        :return:
        """
        return self.__version

    def try_login(self, raise_if_fail=False):
        """
        function to check if login is done.
        If not try to use environment variables by default
        :param raise_if_fail: Boolean, raise if login failed
        or env variables are does not exists. Default False
        :return: OpenTmiClient
        :throws: OpentmiException in case of failure
        """
        # use environment variables if available
        token = os.getenv(ENV_GITHUB_ACCESS_TOKEN)
        if token:
            self.logger.info("Using github access token from environment variable")
            return self.login_with_access_token(access_token=token, service="github")
        username = os.getenv(ENV_OPENTMI_USERNAME)
        password = os.getenv(ENV_OPENTMI_PASSWORD)
        if username and password:
            self.logger.info("Using opentmi credentials from environment variable")
            return self.login(username, password)
        if raise_if_fail:
            raise OpentmiException("login required")
        return self

    @requires_logged_in
    @setter_rules(value_type=Event)
    def post_event(self, event: Event):
        """
        Send build
        :param event: Event object
        :return: Stored event
        """
        data = self._post_json("/events", event.data)
        self.logger.debug("Event uploaded successfully, _id: %s", data.get("_id"))
        return Event.from_data(data)

    @requires_logged_in
    @setter_rules(value_type=Build)
    def post_build(self, build: Build):
        """
        Send build
        :param build: Build object
        :return: Stored build data
        """
        data = self._post_json("/duts/builds", build.data)
        self.logger.debug("build uploaded successfully, _id: %s", data.get("_id"))

    @requires_logged_in
    @setter_rules(value_type=Resource)
    def post_resource(self, resource) -> Resource:
        """
        Send resource
        :param resource: Resource object
        :return: Stored resource data
        """
        data = self._post_json("/resources", resource.data)
        self.logger.debug("resource uploaded successfully, _id: %s", data.get("_id"))
        return Resource.from_data(data)

    @deprecation.deprecated(deprecated_in="v0.7.0", removed_in="v0.8.0",
                            details="Use post_build(Build) instead")
    def upload_build(self, build: dict) -> dict:
        """
        Upload build
        :param build:
        :return:
        """
        build_dict = build
        build = Build()
        build.set_data(build_dict)
        return self.post_build(build).data

    # Suite
    @requires_logged_in
    def get_suite(self, suite, options=''):
        """
        get single suite informations
        :param suite:
        :param options:
        :return:
        """
        try:
            campaigns = self._get_json("/campaigns", {"name": suite})
            assert len(campaigns) == 1, 'did not found campaind'
            campaign_id = campaigns[0]._id
        except OpentmiException as error:
            self.logger.warning("exception happened while resolving suite: %s, %s",
                                suite, error)
            return None

        if campaign_id is None:
            self.logger.warning("could not resolve campaign id for suite: %s",
                                suite)
            return None

        return self._get_json(f"/campaigns/{suite}/suite{options}")

    # Campaign

    # @requires_logged_in
    def get_campaigns(self):
        """
        Get campaigns
        :return:
        """
        return self._get_json("/campaigns")

    @requires_logged_in
    def get_campaign_names(self):
        """
        Get campaign names
        :return:
        """
        return self._get_json("/campaigns", {"f": "name", "t": "distinct"})

    @requires_logged_in
    def get_testcases(self, filters=None):
        """
        Get testcases
        :param filters:
        :return:
        """
        data = self._get_json("/testcases", filters)
        return map(Testcase, data)

    @requires_logged_in
    def get_resources(self, filters=None):
        data = self._get_json('/resources', params=filters)
        return map(Resource, data)

    @requires_logged_in
    def update_testcase(self, testcase):
        """
        update test case
        :param metadata:
        :return:
        """
        testcase = self.__lookup_testcase(testcase.tcid)
        if testcase:
            test_id = testcase._id
            self.logger.info("Update existing TC (%s)", test_id)
            return self.__update_testcase(test_id, testcase)
        else:
            self.logger.info("Create new TC")
            return self._post_json("/testcases", testcase.data)

    @requires_logged_in
    @setter_rules(value_type=Result)
    def post_result(self, result) -> Result:
        """
        Post Result object
        :param result: Result or plain dictionary
        :return:
        """
        files = None
        # hasLogs, logFiles = result.hasLogs()
        # if hasLogs:
        #    zipFile = self.__archiveLogs(logFiles)
        #    self.logger.debug(zipFile)
        #    files = {"file": ("logs.zip", open(zipFile), 'rb') }
        #    self.logger.debug(files)
        data = self._post_json("/results", result.data, files=files)
        self.logger.debug("result uploaded successfully, _id: %s", data.get("_id"))
        return Result.from_data(data)

    @deprecation.deprecated(deprecated_in="v0.7.0", removed_in="v0.8.0",
                            details="Use post_result(Result) instead")
    def upload_results(self, result):
        tc_meta = self.__tc_converter(result.tc_metadata) if self.__tc_converter else result
        result_dict = self.__result_converter(result) if self.__result_converter else result
        the_test = Testcase.from_data(tc_meta)
        the_result = Result.from_data(result_dict)
        self.upload_result_and_ensure_test_exists(the_result, the_test)

    def upload_result_and_ensure_test_exists(self, result: Result, test: Testcase):
        """
        Upload result, and test case if not stored already
        :param result: Result
        :param test: Testcase
        :return: Dictionary
        """
        db_test = self.__lookup_testcase(test.tcid)
        if not db_test:
            db_test = self._post_json("/testcases", test.data)
        if not db_test:
            raise OpentmiException("Cannot create test case")
        return self.post_result(result)

    # Private members
    def _post_json(self, url, payload):
        url = self.__resolve_apiuri(url)
        try:
            data = self.__transport.post_json(url, payload)
            self.logger.debug("Post successfully, _id: %s", payload.get("_id"))
            return data
        except TransportException as error:
            self.logger.warning("Post failed: %s (status: %s)",
                                error.message, error.code)
            raise

    def _put_json(self, url, payload):
        url = self.__resolve_apiuri(url)
        try:
            data = self.__transport.put_json(url, payload)
            self.logger.debug("Put successfully, _id: %s", payload.get("_id"))
            return data
        except TransportException as error:
            self.logger.warning("Put failed: %s (status: %s)",
                                error.message, error.code)
            raise

    def _get_json(self, url, params=None):
        url = self.__resolve_apiuri(url)
        try:
            data = self.__transport.get_json(url, params=params)
            self.logger.debug("Get successfully")
            return data
        except TransportException as error:
            self.logger.warning("Get failed: %s (status: %s)",
                                error.message, error.code)
            raise

    def __lookup_testcase(self, tcid):
        url = self.__resolve_apiuri("/testcases")
        self.logger.debug("Search TC: %s", tcid)
        try:
            data = self.__transport.get_json(url, params={"tcid": tcid})
            if len(data) == 1:
                doc = data[0]
                self.logger.debug("testcase '%s' exists in DB (%s)", tcid, doc.get('_id'))
                return Testcase.from_data(doc)
        except TransportException as error:
            if error.code == 404:
                self.logger.warning("testcase '%s' not found form DB", tcid)
            else:
                self.logger.warning("Test case find failed: %s", error.message)
        except OpentmiException as error:
            self.logger.warning(error)

        return None

    def __update_testcase(self, testcase: Testcase) -> Testcase:
        url = self.__resolve_apiuri(f"/testcases/{testcase._id}")
        try:
            self.logger.debug("Update TC: %s", url)
            data = self.__transport.put_json(url, testcase.data)
            self.logger.debug("testcase metadata uploaded successfully")
            return Testcase.from_data(data)
        except TransportException as error:
            self.logger.debug(error)
        except OpentmiException as error:
            self.logger.debug(error)

        self.logger.warning("testcase metadata upload failed")
        return None

    def __resolve_url(self, path):
        return self.__transport.get_url(path)

    def __resolve_apiuri(self, path):
        return self.__resolve_url(self.__api + str(self.__version) + path)
