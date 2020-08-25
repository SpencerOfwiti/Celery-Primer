from proj.tasks import add, mul, xsum


def test_add():
    res = add.delay(4, 4).get(timeout=10)
    assert res == 8


def test_mul():
    res = mul.delay(4, 2).get(timeout=10)
    assert res == 8


def test_xsum():
    res = xsum.delay([1, 2, 3, 4, 5]).get(timeout=10)
    assert res == 15
