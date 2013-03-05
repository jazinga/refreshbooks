import urllib2 as u

from refreshbooks import exceptions as exc


class Transport(object):
    def __init__(self, url, headers_factory, timeout=10):
        self.url = url
        self.headers_factory = headers_factory
        self.timeout = timeout

    def __call__(self, entity):
        request = u.openurl(
            u.Request(
                url=self.url,
                data=entity,
                headers=self.headers_factory()
            ),
            timeout=self.timeout
        )
        try:
            return u.urlopen(request).read()
        except u.HTTPError, e:
            raise exc.TransportException(e.code, e.read())
