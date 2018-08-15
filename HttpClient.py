# coding=utf-8

import cookielib
import urllib
import urllib2


class HttpClient:

    def __init__(self):
        self.__cookie = cookielib.CookieJar()
        self.__req = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))
        self.__req.addheaders = [
            ('Accept', 'application/javascript, */*;q=0.8'),
            ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
        ]
        urllib2.install_opener(self.__req)

    @staticmethod
    def get(url, refer=None):
        try:
            req = urllib2.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req, timeout=60).read()
        except urllib2.HTTPError, e:
            return e.read()

    @staticmethod
    def post(url, data, refer=None):
        try:
            req = urllib2.Request(url, urllib.urlencode(data))
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req, timeout=60).read()
        except urllib2.HTTPError, e:
            return e.read()

    @staticmethod
    def download(url, savefile):
        output = open(savefile, 'wb')
        output.write(urllib2.urlopen(url).read())
        output.close()

    def getcookie(self, key):
        for c in self.__cookie:
            if c.name == key:
                return c.value
        return ''

    def setcookie(self, key, val, domain):
        ck = cookielib.Cookie(version=0, name=key, value=val, port=None, port_specified=False,
                              domain=domain, domain_specified=False, domain_initial_dot=False, path='/',
                              path_specified=True, secure=False, expires=None, discard=True, comment=None,
                              comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
        self.__cookie.set_cookie(ck)
