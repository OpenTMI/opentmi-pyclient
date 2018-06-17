from opentmi_client.utils.Base import BaseApi, setter_rules
from opentmi_client.api.result.Job import Job
from opentmi_client.api.result.Execution import Execution


class Result(BaseApi):

    def __init__(self,
                 tcid=None,
                 execution=None,
                 tcRef=None,
                 job=None
                 ):
        super(Result, self).__init__()
        self.job = job if job else Job()
        self.execution = execution if execution else Execution()
        if tcid: self.tcid = tcid
        if tcRef: self.tcRef = tcRef
    @property
    def tcid(self):
        return self.get("tcid")

    @tcid.setter
    @setter_rules()
    def tcid(self, value):
        return self.set("tcid", value)

    @property
    def verdict(self):
        if self.execution:
            return self.execution.verdict
        return None

    @verdict.setter
    @setter_rules()
    def verdict(self, value):
        if not self.execution:
            self.execution = Execution()
        self.execution.verdict = value
        return self.execution.verdict

    @property
    def tcRef(self):
        return self.get("tcRef")

    @tcid.setter
    @setter_rules()
    def tcRef(self, value):
        return self.set("tcRef", value)

    @property
    def job(self):
        return self.get("job")

    @job.setter
    @setter_rules(type=Job)
    def job(self, value):
        return self.set("job", value)

    @property
    def execution(self):
        return self.get("exec")

    @execution.setter
    @setter_rules(type=Execution)
    def execution(self, value):
        return self.set("exec", value)

    @property
    def campaign(self):
        return self.get("campaign")

    @campaign.setter
    @setter_rules()
    def campaign(self, value):
        return self.set("campaign", value)

    @property
    def campaignRef(self):
        return self.get("campaignRef")

    @campaignRef.setter
    @setter_rules()
    def campaignRef(self, value):
        return self.set("campaignRef", value)
