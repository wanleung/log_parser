# -*- coding: utf-8 -*-

from log_parser.url import Url
from urllib.parse import urlparse


class Record:
    def __init__(self, enableIPCheck=True):
        self._dict = {}
        self._enableIPCheck = enableIPCheck

    def add(self, path, ip):
        parsedPath = urlparse(path).path
        if (parsedPath in self._dict):
            self._dict[parsedPath].add(ip)
        else:
            myUrlObj = Url(parsedPath)
            myUrlObj.enableIPCheck(self._enableIPCheck)
            myUrlObj.add(ip)
            self._dict[parsedPath] = myUrlObj

    def views(self):
        return {k: v.views() for k, v in self._dict.items()}

    def viewUniq(self):
        return {k: v.viewUniq() for k, v in self._dict.items()}
