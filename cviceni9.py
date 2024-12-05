def sudy_lichy(cislo):
    if cislo % 2 == 0:
        return "sudy"
    else:
        return "lichy"


def test_sudy_lichy():
    assert sudy_lichy(1) == "lichy"
    assert sudy_lichy(2) == "sudy"
    assert sudy_lichy(100) == "sudy"
    assert sudy_lichy(1001) == "lichy"