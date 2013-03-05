import requests

from refreshbooks import exceptions as exc


class Transport(object):
    def __init__(self, url, headers_factory, timeout=10):
        self.session = requests.session()
        self.url = url
        self.headers_factory = headers_factory
        self.timeout = timeout

    def __call__(self, entity):
        resp = self.session.post(
            self.url,
            headers=self.headers_factory(),
            data=entity,
            timeout=self.timeout,
        )
        if resp.status_code >= 400:
            raise exc.TransportException(resp.status_code, resp.content)
        return resp.content
