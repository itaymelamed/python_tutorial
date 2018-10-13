import requests


def test_ping():
    r = requests.get('http://10.0.0.6:5000/ping')
    assert r.text == 'pong'
