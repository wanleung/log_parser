# -*- coding: utf-8 -*-

import os
import re
from log_parser.record import Record


class Parser:
    def __init__(self, enableIPCheck=True):
        self._filename = ''
        self._record = Record(enableIPCheck=enableIPCheck)
        self._error = None

    def load(self, filename):
        if os.path.isfile(filename) and os.access(filename, os.R_OK):
            self._filename = filename
        else:
            raise RuntimeError('File Not Existed')
        self.__parse()

    def hasFile(self):
        return os.path.isfile(self._filename)

    def getViewsResult(self):
        result = self._record.views()
        output = ''
        for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
            output += "{0} {1} visits\n".format(k, str(v))
        return output

    def getViewUniqResult(self):
        result = self._record.viewUniq()
        output = ''
        for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
            output += "{0} {1} unique views\n".format(k, str(v))
        return output

    def hasError(self):
        return self._error is not None

    def getError(self):
        return self._error

    def __parse(self):
        try:
            myfile = open(self._filename)
            line = myfile.readline()
            linenumber = 1
            while line:
                if re.match(r"^\S+\s+\d+\.\d+\.\d+\.\d+", line):
                    data = line.strip().split(" ", 2)
                    try:
                        self._record.add(data[0], data[1])
                    except (RuntimeError, ValueError, AttributeError) as ex:
                        if not self.hasError():
                            self._error = ''
                        self._error += "WARN: Line {0} : {1}\n".format(
                            linenumber,
                            ex
                        )
                else:
                    if not self.hasError():
                        self._error = ''
                    self._error += "WARN: Line {0} : {1}\n".format(
                        linenumber,
                        "line is not in correct format"
                    )
                line = myfile.readline()
                linenumber += 1
        except (IOError) as ex:
            if not self.hasError():
                self._error = ''
            self._error += "{0}\n".format(ex)
        else:
            myfile.close()
