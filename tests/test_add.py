"""
Test the add() function of the calc selfself.
"""
from calculator import add
import pytest

def test_two_plus_two():
    """
    if given 2 as 2 as params , 4 should be returned
    """
    assert add(2, 2) == 4

def test_no_parameters():
    """
    if no parameters are provided , return 0
    """
    assert add() == 0

def test_one_two_three():
    assert add(1, 2, 3) == 6

def test_decimal_values():
    """
    import pytest
    """
    assert add (0.1, 0.1, 0.1) == pytest.approx(0.3)
