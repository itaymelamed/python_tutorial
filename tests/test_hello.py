import requests


def test_ping():
    r = requests.get('http://web:5000/ping')
    assert r.text == 'pong2'
