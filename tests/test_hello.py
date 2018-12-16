import requests


def test_ping():
    r = requests.get('http://web:5000/ping')
    assert r.text == 'pong'


def test_ping_go():
    r = requests.get('http://g4o:80')
    assert 'pong' in r.text
