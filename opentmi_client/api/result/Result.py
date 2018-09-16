"""
OpenTMI Result module
"""
from junitparser import JUnitXml
from junitparser import Failure as JunitFailure
from junitparser import Skipped as JunitSkipped
import json
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.result.Job import Job
from opentmi_client.api.result.Execution import Execution
from opentmi_client.api.result.File import File
from pydash import reduce_, map_keys

class Result(BaseApi):
    """
    Result class
    """
    def __init__(self,
                 tcid=None,
                 tc_ref=None):
        """
        Constructor for Result
        :param tcid: String
        :param execution: Exection
        :param tcRef: String
        :param job: Job
        """
        super(Result, self).__init__()
        self.job = Job()
        self.execution = Execution()
        if tcid:
            self.tcid = tcid
        if tc_ref:
            self.tc_ref = tc_ref

    @staticmethod
    def from_dict(dictionary, reducer=None):
        """
        Create Result from plain dictionary (JSON)
        :param dictionary: Dict
        :param reducer: optional, e.g. lambda result, value, key: result
        :return: Result
        """
        def reducer_func(_result, value, key):
            if isinstance(value, dict):
                new_value = map_keys(value, lambda inner_value, inner_key: "{}.{}".format(key, inner_key))
                return reduce_(new_value, reducer_func, _result)
            else:
                return reducer(_result, value, key)

        result = Result()
        if reducer:
            reduce_(dictionary, reducer_func, result)
        else:
            result.data = dictionary
        return result

    @staticmethod
    def from_jsonfile(json_filename, reducer=None):
        """
        Create Result from plain dictionary (JSON)
        :param json_filename: String, filename
        :param reducer: optional reducer
        :return: Result
        """
        data = json.load(json_filename)
        return Result.from_dict(data, reducer=reducer)

    @staticmethod
    def from_junit_file(junit_filename, wrapper=None):
        """
        Read junit file to list of Result's
        :param junit_filename: String, filename
        :return: [Result]
        """
        xml = JUnitXml.fromfile(junit_filename)
        results_list = []
        for suite in xml:
            # handle suites
            for case in suite:
                # handle cases
                result = Result()
                if wrapper:
                    wrapper(result, case, suite)
                else:
                    result.tcid = case.name
                    result.execution.sut.append_cut(case.classname)
                if case.system_out:
                    file = File()
                    file.data = case.system_out
                    file.name = "system_out"
                    result.execution.append_log(file)
                if case.system_err:
                    file = File()
                    file.data = case.system_err
                    file.name = "system_err"
                    result.execution.append_log(file)
                result.execution.duration = case.time
                if isinstance(case.result, JunitFailure):
                    result.execution.verdict = 'fail'
                elif isinstance(case.result, JunitSkipped):
                    result.execution.verdict = 'skip'
                else:
                    result.execution.verdict = 'pass'
                results_list.append(result)
        return results_list

    def __str__(self):
        """
        Stringify function
        :return: String
        """
        return "{} - {}".format(self.get("tcid", "?"), self.get("exec.verdict", "?"))

    @property
    def tcid(self):
        """
        Getter for test case ID
        :return: String
        """
        return self.get("tcid")

    @tcid.setter
    @setter_rules()
    def tcid(self, value):
        """
        Setter for test case ID
        :param value: String
        """
        self.set("tcid", value)

    @property
    def verdict(self):
        """
        Getter for test verdict
        :return: String
        """
        if self.execution:
            return self.execution.verdict
        return None

    @verdict.setter
    @setter_rules()
    def verdict(self, value):
        """
        Setter for test verdict
        :param value: String
        """
        if not self.execution:
            self.execution = Execution()
        self.execution.verdict = value

    @property
    def tc_ref(self):
        """
        Getter for test reference id
        :return: String
        """
        return self.get("tcRef")

    @tc_ref.setter
    @setter_rules()
    def tc_ref(self, value):
        """
        Setter for test reference
        :param value: String
        """
        self.set("tcRef", value)

    @property
    def job(self):
        """
        Getter for job
        :return: Job
        """
        return self.get("job")

    @job.setter
    @setter_rules(value_type=Job)
    def job(self, value):
        """
        Setter for job
        :param value: Job
        """
        self.set("job", value)

    @property
    def execution(self):
        """
        Getter for execution object
        :return: Execution
        """
        return self.get("exec")

    @execution.setter
    @setter_rules(value_type=Execution)
    def execution(self, value):
        """
        Setter for Execution
        :param value: Execution
        """
        self.set("exec", value)

    @property
    def campaign(self):
        """
        Getter for Campaign
        :return: String
        """
        return self.get("campaign")

    @campaign.setter
    @setter_rules()
    def campaign(self, value):
        """
        Setter for Campaign
        :param value: String
        """
        self.set("campaign", value)

    @property
    def campaign_ref(self):
        """
        Getter for campaign reference
        :return: String
        """
        return self.get("campaignRef")

    @campaign_ref.setter
    @setter_rules()
    def campaign_ref(self, value):
        """
        Setter for campaign ref
        :param value: String
        """
        self.set("campaignRef", value)
