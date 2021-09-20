import pytest
import buss_logic as bl


num1 = 20
num2 = 10


def test_add():
    expected = num1 + num2
    actual = bl.added(num1, num2)
    assert(expected, actual)

def test_multi():
    expected = num1 * num2
    actual = bl.multip(num1, num2)
    assert(expected, actual)

def test_sub():        
    expected = num1 - num2
    actual = bl.subt(num1, num2)
    assert(expected, actual)
    
def test_div():
    expected = num1 / num2
    actual = bl.divi(num1, num2)
    assert(expected, actual)