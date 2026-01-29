import pytest
from computor.models.unknown import Unknown
from computor.models.polynomial import Polynomial

def test_degree_and_str():
    # Polynomial 2x^2 + 3x + 4
    p = Polynomial(Unknown(2, 2), Unknown(3, 1), Unknown(4, 0))
    assert p.get_degree() == 2
    reduced = str(p)
    assert "2 * X^2" in reduced
    assert "3 * X^1" in reduced
    assert "4 * X^0" in reduced

def test_linear_solution(capsys):
    p = Polynomial(Unknown(0, 2), Unknown(2, 1), Unknown(-4, 0))
    p.resolve()
    captured = capsys.readouterr()
    assert "Polynomial degree: 1" in captured.out
    assert "The solution is:" in captured.out
    # solution should be 2.0
    assert "2.000000" in captured.out

def test_quadratic_positive_discriminant(capsys):
    # x^2 - 3x + 2 = 0 -> solutions 1 and 2
    p = Polynomial(Unknown(1, 2), Unknown(-3, 1), Unknown(2, 0))
    p.resolve()
    captured = capsys.readouterr()
    assert "Polynomial degree: 2" in captured.out
    assert "Discriminant is strictly positive" in captured.out
    assert "1.000000" in captured.out
    assert "2.000000" in captured.out

def test_quadratic_zero_discriminant(capsys):
    # x^2 - 2x + 1 = 0 -> solution 1
    p = Polynomial(Unknown(1, 2), Unknown(-2, 1), Unknown(1, 0))
    p.resolve()
    captured = capsys.readouterr()
    assert "Discriminant is equal to zero" in captured.out
    assert "1.000000" in captured.out

def test_quadratic_negative_discriminant(capsys):
    # x^2 + x + 1 = 0 -> complex solutions
    p = Polynomial(Unknown(1, 2), Unknown(1, 1), Unknown(1, 0))
    p.resolve()
    captured = capsys.readouterr()
    assert "Discriminant is strictly negative" in captured.out
    assert "+" in captured.out
    assert "-" in captured.out

def test_degree_zero_solutions(capsys):
    # 0 = 0 -> all solutions
    p = Polynomial(Unknown(0, 2), Unknown(0, 1), Unknown(0, 0))
    p.resolve()
    captured = capsys.readouterr()
    assert "Any real number is a solution" in captured.out

    # 5 = 0 -> no solution
    p2 = Polynomial(Unknown(0, 2), Unknown(0, 1), Unknown(5, 0))
    p2.resolve()
    captured = capsys.readouterr()
    assert "No solution" in captured.out
