def test_validate():
    assert 2 == 2


def test_fail():
    assert 2 == 4


def test_selnium(selenium):
    selenium.get('http://www.ynet.co.il')
    assert False
