#!/usr/bin/env python

import pytest
from log_parser.record import Record


@pytest.fixture
def myRecordObj():
    return Record()


@pytest.fixture
def myNoIPCheckRecordObj():
    return Record(enableIPCheck=False)


@pytest.fixture
def myFilledRecordObj():
    recordObj = Record()
    recordObj.add('/a', '10.0.0.1')
    recordObj.add('/b', '10.0.0.2')
    recordObj.add('/b', '10.0.0.3')
    recordObj.add('/c', '10.0.0.4')
    recordObj.add('/c', '10.0.0.5')
    recordObj.add('/c', '10.0.0.6')
    recordObj.add('/d', '10.0.0.7')
    recordObj.add('/d', '10.0.0.8')
    recordObj.add('/d', '10.0.0.9')
    recordObj.add('/d', '10.0.0.10')
    return recordObj


def test_add_to_record_and_get_view_count(myRecordObj):
    myRecordObj.add('/home/1', '127.0.0.1')
    assert myRecordObj.views() == {'/home/1': 1}


def test_add_to_record_and_get_view_count_2(myRecordObj):
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '192.168.0.1')
    myRecordObj.add('/home/2', '127.0.0.1')
    myRecordObj.add('/home/2', '192.168.0.1')
    assert myRecordObj.views() == {'/home/1': 3, '/home/2': 2}


def test_add_to_record_and_get_view_uniq_count(myRecordObj):
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '192.168.0.1')
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '192.168.0.1')
    assert myRecordObj.viewUniq() == {'/home/1': 2}


def test_add_to_record_and_get_view_uniq_count_2(myRecordObj):
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '127.0.0.1')
    myRecordObj.add('/home/1', '192.168.0.1')
    myRecordObj.add('/home/2', '192.168.0.1')
    myRecordObj.add('/home/2', '192.168.0.1')
    assert myRecordObj.viewUniq() == {'/home/1': 2, '/home/2': 1}


def test_record_views(myFilledRecordObj):
    assert myFilledRecordObj.views() == {'/d': 4, '/c': 3, '/b': 2, '/a': 1}


def test_record_view_uniq(myFilledRecordObj):
    assert myFilledRecordObj.viewUniq() == {'/d': 4, '/c': 3, '/b': 2, '/a': 1}


def test_wrong_type_path(myRecordObj):
    with pytest.raises(AttributeError):
        myRecordObj.add(12345, '127.0.0.1')


def test_not_vaild_ip(myRecordObj):
    with pytest.raises(ValueError):
        myRecordObj.add('/', '888.888.888.888')


def test_disable_ip_check(myNoIPCheckRecordObj):
    myNoIPCheckRecordObj.add('/', '888.888.888.888')
    assert myNoIPCheckRecordObj.views() == {'/': 1}
