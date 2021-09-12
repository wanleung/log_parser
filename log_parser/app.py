# -*- coding: utf-8 -*-

from log_parser.parser import Parser


class App:
    def __init__(
        self, infile,
        enableIPCheck=True,
        outfile=None,
        errorfile=None
    ):
        self.infile = infile
        self.enableIPCheck = enableIPCheck
        self.outfile = outfile
        self.errorfile = errorfile
        self.parser = Parser(enableIPCheck=self.enableIPCheck)

    def run(self):
        self.parser.load(self.infile)
        print(self.parser.getViewsResult())
        print(self.parser.getViewUniqResult())
        if self.outfile:
            self._exportResult()
        if self.parser.hasError():
            print(self.parser.getError())
            if self.errorfile:
                self._exportError()

    def _exportResult(self):
        output = self.parser.getViewsResult()
        output += "\n"
        output += self.parser.getViewUniqResult()
        self._export(output, self.outfile)

    def _exportError(self):
        if self.parser.hasError():
            self._export(self.parser.getError(), self.errorfile)

    def _export(self, output, outfile):
        fp = open(outfile, 'w')
        fp.write(output)
        fp.close
