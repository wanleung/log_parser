#!/usr/bin/env python

import pytest
from log_parser.parser import Parser


def test_create_Parser_Object():
    parser = Parser()
    assert parser


def test_load_file():
    with pytest.raises(RuntimeError):
        parser = Parser()
        parser.load("nofile")


def test_load_file_none():
    parser = Parser()
    assert not parser.hasFile()


def test_load_file_exists(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text("/a 127.0.0.1")

    parser = Parser()
    parser.load(f1)
    assert parser.hasFile()


def test_parse_file(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''/a 127.0.0.1
/a 127.0.0.1
/b 10.0.0.1
/b 10.0.0.2
/b 10.0.0.2
/c 10.0.0.1
/c 10.0.0.1
/d 10.0.0.1
/d 10.0.0.2
/d 10.0.0.2
/d 10.0.0.1
''')

    parser = Parser()
    parser.load(f1)
    assert parser.hasFile()
    result = parser.getViewsResult()
    assert result == '''/d 4 visits
/b 3 visits
/a 2 visits
/c 2 visits
'''

    resultUniq = parser.getViewUniqResult()
    assert resultUniq == '''/b 2 unique views
/d 2 unique views
/a 1 unique views
/c 1 unique views
'''


def test_parse_file_invild_ip(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''/a 888.888.888.888
/a 127.0.0.1
/b 300.300.000.000
/b 10.0.0.2
/b 10.0.0.2
/c 10.0.0.1
/c 500.500.500.500
/d 10.0.0.1
/d 10.0.0.2
/d 300.300.300.300
/d 10.0.0.1
''')

    parser = Parser()
    parser.load(f1)
    assert parser.hasFile()
    result = parser.getViewsResult()
    assert result == '''/d 3 visits
/b 2 visits
/a 1 visits
/c 1 visits
'''

    resultUniq = parser.getViewUniqResult()
    assert resultUniq == '''/d 2 unique views
/a 1 unique views
/b 1 unique views
/c 1 unique views
'''

    assert parser.hasError()
    assert parser.getError() is not None


def test_parse_file_invild_ip_for_disable_ip_check(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''/a 888.888.888.888
/a 127.0.0.1
/b 300.300.000.000
/b 10.0.0.2
/b 10.0.0.2
/c 10.0.0.1
/c 500.500.500.500
/d 10.0.0.1
/d 10.0.0.2
/d 300.300.300.300
/d 10.0.0.1
''')

    parser = Parser(enableIPCheck=False)
    parser.load(f1)
    assert parser.hasFile()
    result = parser.getViewsResult()
    assert result == '''/d 4 visits
/b 3 visits
/a 2 visits
/c 2 visits
'''

    resultUniq = parser.getViewUniqResult()
    assert resultUniq == '''/d 3 unique views
/a 2 unique views
/b 2 unique views
/c 2 unique views
'''

    assert not parser.hasError()
    assert parser.getError() is None


def test_parse_file_not_log_format(tmp_path):
    f1 = tmp_path / "mydir/mylog"
    f1.parent.mkdir()
    f1.touch()
    f1.write_text('''ThisisaTest
/aaaa2 2222222 eeeeee
/a 127.0.0.1
/b 300.300.000.000
''')

    parser = Parser()
    parser.load(f1)
    assert parser.hasFile()
    result = parser.getViewsResult()
    assert result == '''/a 1 visits
'''
    assert parser.hasError()
    assert parser.getError() is not None
