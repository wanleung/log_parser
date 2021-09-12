#!/usr/bin/env python

import pytest
import re
from log_parser.app import App


def test_create_app():
    app1 = App("InFile.txt")
    assert app1.enableIPCheck is True
    assert "InFile.txt" == app1.infile
    assert app1.outfile is None
    assert app1.errorfile is None

    with pytest.raises(TypeError):
        app2 = App()
        assert app2.enableIPCheck is True

    app3 = App("InFile.txt", enableIPCheck=False)
    assert app3.enableIPCheck is False
    assert "InFile.txt" == app3.infile
    assert app3.outfile is None
    assert app3.errorfile is None

    app4 = App("InFile.txt", outfile="OutFile.txt")
    assert app4.enableIPCheck is True
    assert "InFile.txt" == app4.infile
    assert "OutFile.txt" == app4.outfile
    assert app4.errorfile is None

    app5 = App("InFile.txt", outfile="OutFile.txt", errorfile="ErrorFile.txt")
    assert app5.enableIPCheck is True
    assert "InFile.txt" == app5.infile
    assert "OutFile.txt" == app5.outfile
    assert "ErrorFile.txt" == app5.errorfile

    app6 = App("InFile.txt", errorfile="ErrorFile.txt")
    assert app6.enableIPCheck is True
    assert "InFile.txt" == app6.infile
    assert app6.outfile is None
    assert "ErrorFile.txt" == app6.errorfile


def test_run_nofile():
    with pytest.raises(RuntimeError):
        app1 = App("InFile.txt")
        app1.run()


def test_run_file(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''ThisisaTest
/aaaa2 2222222 eeeeee
/a 127.0.0.1
/b 300.300.000.000
''')
    app1 = App(f1)
    app1.run()


def test_run_file_with_outfile(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''ThisisaTest
/aaaa2 2222222 eeeeee
/a 127.0.0.1
/b 300.300.000.000
''')
    app1 = App(f1, outfile=tmp_path / "output.txt")
    app1.run()

    of1 = tmp_path / "output.txt"
    myfile = open(of1)
    line = myfile.read()
    assert line == "/a 1 visits\n\n/a 1 unique views\n"


def test_run_file_with_outfile_errorfile(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''ThisisaTest
/aaaa2 2222222 eeeeee
/a 127.0.0.1
/b 300.300.000.000
''')
    app1 = App(
        f1,
        outfile=tmp_path / "output.txt",
        errorfile=tmp_path / "error.txt"
    )
    app1.run()

    of1 = tmp_path / "output.txt"
    myfile = open(of1)
    line = myfile.read()
    assert line == "/a 1 visits\n\n/a 1 unique views\n"

    myfile2 = open(tmp_path / "error.txt")
    line2 = myfile2.readline()
    assert re.match(r"WARN: Line 1 :", line2) is not None
    line2 = myfile2.readline()
    assert re.match(r"WARN: Line 2 :", line2) is not None
    line2 = myfile2.readline()
    assert re.match(r"WARN: Line 4 :", line2) is not None


def test_run_file_with_outfile_errorfile_disable_IP_check(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''ThisisaTest
/aaaa2 2222222 eeeeee
/a 127.0.0.1
/b 300.300.000.000
''')
    app1 = App(
        f1,
        outfile=tmp_path / "output.txt",
        errorfile=tmp_path / "error.txt",
        enableIPCheck=False
    )
    app1.run()

    of1 = tmp_path / "output.txt"
    myfile = open(of1)
    line = myfile.read()
    assert line == '''/a 1 visits
/b 1 visits

/a 1 unique views
/b 1 unique views
'''

    myfile2 = open(tmp_path / "error.txt")
    line2 = myfile2.readline()
    assert re.match(r"WARN: Line 1 :", line2) is not None
    line2 = myfile2.readline()
    assert re.match(r"WARN: Line 2 :", line2) is not None
