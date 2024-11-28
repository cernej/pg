from aplikace import soucet, fibonachi

def test_soucet_2():
    assert soucet(1, 1) == 2

def test_soucet_3():
    assert soucet(1, 2) == 3

def test_fibonachi_5():
    assert fibonachi(5) == [1, 1, 2, 3, 5]

def test_fibonachi_10():
    assert fibonachi(10) == [1, 1, 2, 3, 5, 8]



