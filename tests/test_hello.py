import requests


def test_ping():
    r = requests.get('http://web:5000/ping')
    assert r.text == 'pong'


def test_ping_go():
    r = requests.get('http://go:80')
    assert r.text == 'pong'
