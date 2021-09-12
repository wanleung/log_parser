#!/usr/bin/env python

import pytest

from log_parser.url import Url


def test_create_url_object_and_get_back_url():
    myUrl = Url('/home/1')
    result = myUrl.path
    assert result == '/home/1'


def test_create_url_object_with_query_url():
    myUrl = Url('/home/2?name=bob')
    result = myUrl.path
    assert result == '/home/2'


def test_create_url_object_with_fragment_url():
    myUrl = Url('/home/2#bar')
    result = myUrl.path
    assert result == '/home/2'


def test_create_url_object_with_other_case():
    myUrl = Url('3.1245677?bbb=ccc#ccc')
    result = myUrl.path
    assert result == '3.1245677'


def test_create_url_input_number():
    with pytest.raises(AttributeError):
        Url(3.1245677)


def test_is_same_url_of_two_url_object():
    myUrl1 = Url('/home/1')
    myUrl2 = Url('/home/1')
    assert myUrl1 == myUrl2


def test_if_add_not_vaild_ip():
    with pytest.raises(ValueError):
        myUrl = Url('/home/1')
        myUrl.add("888.999.000.222")


def test_if_add_not_vaild_ip_2():
    with pytest.raises(ValueError):
        myUrl = Url('/home/1')
        myUrl.add("192.168.000.1")


def test_if_add_not_vaild_ip_3():
    with pytest.raises(ValueError):
        myUrl = Url('/home/1')
        myUrl.add("I am a ip")


def test_to_default_ip_check():
    myUrl = Url('/home/1')
    assert myUrl.isIPCheckEnabled()


def test_to_set_ip_check_enable():
    myUrl = Url('/home/1')
    myUrl.enableIPCheck(False)
    assert not myUrl.isIPCheckEnabled()
    myUrl.enableIPCheck(True)
    assert myUrl.isIPCheckEnabled()


def test_to_disable_ip_check():
    myUrl = Url('/home/1')
    myUrl.enableIPCheck(False)
    myUrl.add("888.888.888.888")
    assert 1 == myUrl.views()


@pytest.fixture
def myUrlObj():
    return Url('/home/1')


def test_add_ip(myUrlObj):
    myUrlObj.add("127.0.0.1")
    assert 1 == myUrlObj.views()


def test_view(myUrlObj):
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("127.0.0.1")
    assert 2 == myUrlObj.views()


def test_view_2(myUrlObj):
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("192.168.0.1")
    assert 3 == myUrlObj.views()


def test_view_uniq(myUrlObj):
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("127.0.0.1")
    assert 1 == myUrlObj.viewUniq()


def test_view_uniq_2(myUrlObj):
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("127.0.0.1")
    myUrlObj.add("192.168.0.1")
    assert 2 == myUrlObj.viewUniq()
