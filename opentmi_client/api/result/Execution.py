"""
OpenTMI module for Result Execution
"""
from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules
from opentmi_client.api.result.File import File
from opentmi_client.api.result.Environment import Environment


class Execution(BaseApi):
    """
    Execution class,
    holds details about test execution phase
    """
    def __init__(self,
                 verdict=None,
                 note=None,
                 duration=None,
                 environment=None):
        """
        Execution constructor
        :param verdict: String
        :param note: : String
        :param duration: float
        :param environment: Environment
        """
        super(Execution, self).__init__()
        if verdict:
            self.verdict = verdict
        if note:
            self.note = note
        if duration:
            self.duration = duration
        self.environment = environment if environment else Environment()

    @property
    def verdict(self):
        """
        Getter for test verdict
        :return: String
        """
        return self.get("verdict")

    @verdict.setter
    @setter_rules(enum='pass fail inconclusive blocked error skip')
    def verdict(self, value):
        """
        Setter for test verdict
        :param value: String (allowed values: pass, fail, inconclusive, blocked, error, skip)
        """
        self.set("verdict", value)

    @property
    def note(self):
        """
        Getter for notes. Eg notes why test fails
        :return: String
        """
        return self.get("note")

    @note.setter
    @setter_rules()
    def note(self, value):
        """
        Setter for test notes
        :param value: String
        """
        self.set("note", value)

    @property
    def duration(self):
        """
        Getter for test duration
        :return: float
        """
        return self.get("duration")

    @duration.setter
    @setter_rules(type=float)
    def duration(self, value):
        """
        Setter for duration
        :param value: float
        """
        self.set("duration", value)

    @property
    def profiling(self):
        """
        Getter for profiling
        :return: dict
        """
        return self.get("profiling")

    @profiling.setter
    @setter_rules(type=dict)
    def profiling(self, value):
        """
        Setter for profiling.
        Profiling could contains eg timespans for different test phases:
        eg: {"setUp": {"duration": 10}}
        :param value: dict
        """
        self.set("profiling", value)

    @property
    def logs(self):
        """
        Getter for logs
        :return: List<File>
        """
        return self.get("logs")

    @logs.setter
    @setter_rules(type=list, each_type=File)
    def logs(self, value):
        """
        Setter for logs
        :param value: List<File>
        """
        self.set("logs", value)

    def append_log(self, log_file):
        """
        Appens new file to logs array
        :param log_file: File
        """
        assert isinstance(log_file, File), "require File instance"
        if not isinstance(self.logs, list):
            self.logs = []
        self.logs.append(log_file)

    @property
    def environment(self):
        """
        Getter for environment
        :return: Environment
        """
        return self.get("env")

    @environment.setter
    @setter_rules(type=Environment)
    def environment(self, value):
        """
        Setter for environment
        :param value: Environment
        """
        self.set("env", value)
