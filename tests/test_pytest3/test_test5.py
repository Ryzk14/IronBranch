import pytest
import test_class

my_coin = test_class.Coin()


def test_function7(initial_value):
    assert my_coin.set_function1() + initial_value == 3


def test_function8(initial_value):
    ado + var == 7


def test_function9(initial_value):
    ado + var == 7


def test_function10(initial_value):
    assert my_coin.set_function4() + initial_value == 9

def test_function11(initial_value):
    assert my_coin.set_function4() + initial_value == 9

def test_function12(initial_value):
    assert my_coin.set_function5() + initial_value == 11

#@pytest.mark.skip()
def test_function13(initial_value):
    assert my_coin.set_function6() + initial_value == 13

def test_function14(initial_value):
    assert my_coin.set_function6() + initial_value == 131
