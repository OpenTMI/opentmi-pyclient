from opentmi_client.utils.Base import BaseApi
from opentmi_client.utils.decorators import setter_rules


class Vcs(BaseApi):

    @property
    def name(self):
        return self.get("name")

    @name.setter
    @setter_rules()
    def name(self, value):
        return self.set("name", value)

    @property
    def system(self):
        return self.get("system")

    @system.setter
    @setter_rules(enum="git SVN CSV")
    def system(self, value):
        return self.set("system", value)

    @property
    def type(self):
        return self.get("type")

    @type.setter
    @setter_rules(enum="PR")
    def type(self, value):
        return self.set("type", value)

    @property
    def commitId(self):
        return self.get("commitId")

    @commitId.setter
    @setter_rules()
    def commitId(self, value):
        return self.set("commitId", value)

    @property
    def branch(self):
        return self.get("branch")

    @branch.setter
    @setter_rules()
    def branch(self, value):
        return self.set("branch", value)

    @property
    def base_branch(self):
        return self.get("base_branch")

    @base_branch.setter
    @setter_rules()
    def base_branch(self, value):
        return self.set("base_branch", value)

    @property
    def base_commit(self):
        return self.get("base_commit")

    @base_commit.setter
    @setter_rules()
    def base_commit(self, value):
        return self.set("base_commit", value)

    @property
    def pr_number(self):
        return self.get("pr_number")

    @pr_number.setter
    @setter_rules()
    def pr_number(self, value):
        return self.set("pr_number", value)

    @property
    def url(self):
        return self.get("url")

    @url.setter
    @setter_rules()
    def url(self, value):
        return self.set("url", value)

    @property
    def clean_wa(self):
        return self.get("clean_wa")

    @clean_wa.setter
    @setter_rules(type=bool)
    def clean_wa(self, value):
        return self.set("clean_wa", value)
