import pytest
from computor.models.unknown import Unknown
from computor.models.polynomial import Polynomial
from computor.parser.parser import Parser

def test_degree_zero(capsys):
    # 0 = 0
    parser = Parser("0 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Any real number is a solution" in captured.out

    # 5 = 0
    parser = Parser("5 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "No solution" in captured.out

def test_linear_positive_solution(capsys):
    # 2 * X + 4 = 0 -> x = -2
    parser = Parser("2 * X + 4 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Polynomial degree: 1" in captured.out
    assert "-2.000000" in captured.out

def test_linear_negative_solution(capsys):
    # -3 * X + 6 = 0 -> x = 2
    parser = Parser("-3 * X + 6 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Polynomial degree: 1" in captured.out
    assert "2.000000" in captured.out

def test_quadratic_positive_discriminant(capsys):
    # X^2 - 3*X + 2 = 0 -> x = 1 and 2
    parser = Parser("X^2 - 3 * X + 2 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Polynomial degree: 2" in captured.out
    assert "Discriminant is strictly positive" in captured.out
    assert "1.000000" in captured.out
    assert "2.000000" in captured.out

def test_quadratic_zero_discriminant(capsys):
    # X^2 - 2*X + 1 = 0 -> x = 1
    parser = Parser("X^2 - 2 * X + 1 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Discriminant is equal to zero" in captured.out
    assert "1.000000" in captured.out

def test_quadratic_negative_discriminant(capsys):
    # X^2 + X + 1 = 0 -> complex solutions
    parser = Parser("X^2 + X + 1 = 0")
    parser.parse()
    captured = capsys.readouterr()
    assert "Discriminant is strictly negative" in captured.out
    assert "+" in captured.out and "-" in captured.out

def test_rhs_handling(capsys):
    # 1 = X -> x = 1
    parser = Parser("1 = X")
    parser.parse()
    captured = capsys.readouterr()
    assert "Polynomial degree: 1" in captured.out
    assert "1.000000" in captured.out

def test_syntax_error():
    # invalid symbol
    parser = Parser("X $ 5 = 0")
    with pytest.raises(KeyError):
        parser.parse()
