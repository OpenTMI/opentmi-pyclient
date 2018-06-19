"""
OpenTMI Result module
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.result.Job import Job
from opentmi_client.api.result.Execution import Execution, File


class Result(BaseApi):
    """
    Result class
    """
    def __init__(self,
                 tcid=None,
                 execution=None,
                 tc_ref=None,
                 job=None):
        """
        Constructor for Result
        :param tcid: String
        :param execution: Exection
        :param tcRef: String
        :param job: Job
        """
        super(Result, self).__init__()
        self.job = job if job else Job()
        self.execution = execution if execution else Execution()
        if tcid:
            self.tcid = tcid
        if tc_ref:
            self.tc_ref = tc_ref

    def __str__(self):
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
    @setter_rules(type=Job)
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
    @setter_rules(type=Execution)
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
