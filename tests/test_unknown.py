import pytest
from math import isclose

from computor.models.unknown import Unknown

def test_creation_and_attributes():
    u = Unknown(3, 2)
    assert u.coef == 3
    assert u.degree == 2

def test_str_and_repr():
    assert str(Unknown(0, 2)) == ""
    assert str(Unknown(1, 0)) == "1"
    assert str(Unknown(1, 1)) == "x"
    assert str(Unknown(1, 2)) == "x²"
    assert str(Unknown(2, 3)) == "2x^3"
    assert repr(Unknown(3, 2)) == "Unknown(3.0, 2)"

def test_float_and_neg():
    u = Unknown(5, 3)
    assert float(u) == 5
    neg_u = -u
    assert neg_u.coef == -5
    assert neg_u.degree == 3

def test_addition():
    u = Unknown(2, 1)
    assert (u + 3).coef == 5
    assert (3 + u).coef == 5

def test_subtraction():
    u = Unknown(5, 2)
    assert (u - 2).coef == 3
    assert (10 - u).coef == 5

def test_multiplication():
    u = Unknown(4, 1)
    assert (u * 2).coef == 8
    assert (3 * u).coef == 12

def test_division():
    u = Unknown(8, 2)
    assert (u / 2).coef == 4
    with pytest.raises(ZeroDivisionError):
        _ = u / 0

def test_comparisons():
    u = Unknown(5, 1)
    assert u == 5
    assert u < 6
    assert u > 4

def test_operate_helper_indirectly():
    u = Unknown(3, 2)
    assert (u + 2).coef == 5
    assert (u - 1).coef == 2
    assert (u * 2).coef == 6
    assert (u / 3).coef == 1
