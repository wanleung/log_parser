# -*- coding: utf-8 -*-

from urllib.parse import urlparse
import ipaddress


class Url:
    def __init__(self, url):
        parsedUrl = urlparse(url)
        self.path = parsedUrl.path
        self._set = set()
        self._views = 0
        self._enableIPCheck = True

    def __eq__(self, other):
        return self.path == other.path

    def add(self, ipAddress):
        if self._enableIPCheck:
            ip = ipaddress.ip_address(ipAddress)
        else:
            ip = ipAddress
        self._views += 1
        self._set.add(ip)

    def views(self):
        return self._views

    def viewUniq(self):
        return len(self._set)

    def enableIPCheck(self, enable):
        self._enableIPCheck = enable

    def isIPCheckEnabled(self):
        return self._enableIPCheck
