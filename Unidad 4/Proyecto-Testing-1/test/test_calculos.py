import pytest
from calculos  import suma, divide

def test_suma():
    assert suma(2, 3) == 5

def test_suma_invalido():
    assert suma(2, 3) == 6

def test_divide_ok():
    assert divide(10, 2) == 5