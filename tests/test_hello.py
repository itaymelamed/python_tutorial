import requests


def test_ping():
    r = requests.get('http://app:5000/ping')
    assert r.text == 'pong2'
