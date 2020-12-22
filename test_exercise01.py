# import pytest
from exercise01 import repeats

def test_exercise_check_with_singles():

    assert repeats([4,5,7,5,4,8]) == 15
    assert repeats([9, 10, 19, 13, 19, 13]) == 19
    assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
    assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) == 22
    assert repeats([5, 10, 19, 13, 10, 13]) == 24

def test_exercise_check_with_no_valid_singles():
    assert repeats([6, 6, 8, 8]) == 0