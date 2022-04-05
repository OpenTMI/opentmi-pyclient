import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import urllib.parse

DEFAULT_TIMEOUT = 30  # seconds


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def create_http_session(base_url: str) -> requests.Session:
    """
    @example
    > s = create_http_session('http://localhost', 'mytoken')
    > s.get(s.base_url_join('/api'))
    :param base_url:
    :param token:
    :return:
    """
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    retry_adapter = TimeoutHTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount(base_url, retry_adapter)
    session.headers.update({"content-type": "application/json",
                            "Connection": "keep-alive"
    })
    session.base_url_join = lambda path: urllib.parse.urljoin(base_url, path)
    return session
