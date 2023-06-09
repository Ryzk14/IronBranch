import pytest
import test_class

my_coin = test_class.Coin()


def test_function1(initial_value):
    assert my_coin.set_function1() + initial_value == 3


def test_function2(initial_value):
    assert my_coin.set_function2() + initial_value == 5


def test_function3(initial_value):
    assert my_coin.set_function3() + initial_value == 7


def test_function4(initial_value):
    assert my_coin.set_function4() + initial_value == 9


def test_function5(initial_value):
    assert my_coin.set_function5() + initial_value == 11

#@pytest.mark.skip()
def test_function6(initial_value):
    assert my_coin.set_function6() + initial_value == 13

def test_function7(initial_value):
    assert my_coin.set_function6() + initial_value == 14
