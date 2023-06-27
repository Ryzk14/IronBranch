import test_class

my_coin = test_class.Coin()


def test_function15(initial_value):
    assert my_coin.set_function1() + initial_value == 3



def test_function16(initial_value):
    assert my_coin.set_function3() + float(initial_value) == 7


def test_function17(initial_value):
    assert my_coin.set_function4() + initial_value == 9


def test_function18(initial_value):
    assert my_coin.set_function5() + initial_value == 11


def test_function19(initial_value):
    assert my_coin.set_function6() + initial_value == 14
