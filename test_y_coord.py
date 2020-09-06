import pytest
from y_coord import find_y, find_slope, find_y_3

def test_find_y():
    expected = 1
    answer = find_y((0,0), (2,2), 1)
    assert answer == expected

def test_find_m():
    answer = find_slope((0,0), (2,2))
    expected = 1
    assert answer == expected

def test_find_y_3():
    answer = find_y_3((0,0), 1, 1)
    expected = 1
    assert answer == expected
