from src.math_operations import add, sub
import pytest
from pytest import assert

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(-5,-7) == -12

def test_sub():
    assert sub(5,3) == 2
    assert sub(9,11) == -2 
    assert sub(1,11) == -10