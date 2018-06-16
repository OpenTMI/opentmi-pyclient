from opentmi_client.utils.Base import BaseApi, setter_rules

from opentmi_client.api.result.File import File
from opentmi_client.api.result.Environment import Environment


class Execution(BaseApi):
    def __init__(self,
                 verdict=None,
                 note=None,
                 duration=None,
                 env=None):
        super(Execution, self).__init__()
        if verdict: self.verdict = verdict
        if note: self.note = note
        if duration: self.duration = duration
        if env: self.env = env


    @property
    def verdict(self):
        return self.get("verdict")
    @verdict.setter
    @setter_rules(enum='pass fail inconclusive blocked error skip')
    def verdict(self, value):
        return self.set("verdict", value)

    @property
    def note(self):
        return self.get("note")
    @note.setter
    @setter_rules()
    def note(self, value):
        return self.set("note", value)

    @property
    def duration(self):
        return self.get("duration")
    @duration.setter
    @setter_rules(type=float)
    def duration(self, value):
        return self.set("duration", value)

    @property
    def profiling(self):
        return self.get("profiling")

    @profiling.setter
    @setter_rules(type=dict)
    def profiling(self, value):
        return self.set("profiling", value)

    @property
    def logs(self):
        return self.get("logs")

    @logs.setter
    @setter_rules(type=list, each_type=File)
    def logs(self, value):
        return self.set("logs", value)

    @property
    def env(self):
        return self.get("env")

    @env.setter
    @setter_rules(type=Environment)
    def env(self, value):
        return self.set("env", value)
