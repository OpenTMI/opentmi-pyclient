from opentmi_client.utils.Base import BaseApi, setter_rules
from opentmi_client.api.result import Job, Execution


class Result(BaseApi):

    def __init__(self,
                 tcid=None,
                 exec=None,
                 tcRef=None,
                 job=None
                 ):
        super(Result, self).__init__()
        if tcid: self.tcid = tcid
        if exec: self.exec = exec
        if tcRef: self.tcRef = tcRef
        if job: self.job = job

    @property
    def tcid(self):
        return self.get("tcid")

    @tcid.setter
    @setter_rules()
    def tcid(self, value):
        return self.set("tcid", value)

    @property
    def verdict(self):
        if self.exec:
            return self.exec.verdict
        return None

    @verdict.setter
    @setter_rules()
    def verdict(self, value):
        if not self.exec:
            self.exec = Execution()
        self.exec.verdict = value
        return self.exec.verdict

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
    def exec(self):
        return self.get("exec")

    @exec.setter
    @setter_rules(type=Execution)
    def exec(self, value):
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
