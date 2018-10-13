import requests


def test_ping():
    r = requests.get('http://localhost:5000/ping')
    assert r.text == 'pong'
