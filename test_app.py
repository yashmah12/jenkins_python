from app import *

def test_add():
    assert add(2,6) == 8

def test_subtract():
    assert subtract(9, 3) == 6

def test_multiply():
    assert multiply(2, 12) == 24

def test_divide():
    assert divide(10,2) == 5
