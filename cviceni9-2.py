# prevod stupnu C na F
# F = C * 9 / 5 + 32


def prevod_c_na_f(stupne):
    return stupne * 9 / 5 + 32


def test_prevod_c_na_f():
    assert prevod_c_na_f(100) == 212
    assert prevod_c_na_f(0) == 32