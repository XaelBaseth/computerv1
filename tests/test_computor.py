import subprocess
import textwrap

CMD = ["python", "src/computor.py"]

def run(expr: str) -> str:
    completed = subprocess.run(
        CMD + [expr],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert completed.stderr == ""
    return completed.stdout.strip()

def test_positive_discriminant():
    expected = textwrap.dedent("""\
        Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
        Polynomial degree: 2
        Discriminant is strictly positive, the two solutions are:
        0.905239
        -0.475131
    """).strip()

    output = run("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
    assert output == expected

def test_degree_1():
    expected = textwrap.dedent("""\
        Reduced form: 1 * X^0 + 4 * X^1 = 0
        Polynomial degree: 1
        The solution is:
        -0.25
    """).strip()

    output = run("5 * X^0 + 4 * X^1 = 4 * X^0")
    assert output == expected

def test_degree_3():
    expected = textwrap.dedent("""\
        Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
        Polynomial degree: 3
        The polynomial degree is strictly greater than 2, I can't solve.
    """).strip()

    output = run("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
    assert output == expected

def test_infinite_solutions():
    expected = textwrap.dedent("""\
        Reduced form: 0 * X^0 = 0
        Any real number is a solution.
    """).strip()

    output = run("6 * X^0 = 6 * X^0")
    assert output == expected

def test_no_solution():
    expected = textwrap.dedent("""\
        Reduced form: -5 * X^0 = 0
        No solution.
    """).strip()

    output = run("10 * X^0 = 15 * X^0")
    assert output == expected

def test_negative_discriminant():
    expected = textwrap.dedent("""\
        Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0
        Polynomial degree: 2
        Discriminant is strictly negative, the two complex solutions are:
        -1/5 + 2i/5
        -1/5 - 2i/5
    """).strip()

    output = run("1 * X^0 + 2 * X^1 + 5 * X^2 = 0")
    assert output == expected

def test_zero_discriminant():
    expected = textwrap.dedent("""\
        Reduced form: 1 * X^0 - 2 * X^1 + 1 * X^2 = 0
        Polynomial degree: 2
        Discriminant is equal to zero, the solution is:
        1.000000
    """).strip()
    output = run("1 * X^0 - 2 * X^1 + 1 * X^2 = 0")
    assert output == expected

def test_pure_quadratic():
    expected = textwrap.dedent("""\
        Reduced form: -4 * X^0 + 0 * X^1 + 1 * X^2 = 0
        Polynomial degree: 2
        Discriminant is strictly positive, the two solutions are:
        -2.000000
        2.000000
    """).strip()
    output = run("1 * X^2 = 4 * X^0")  # x^2 - 4 = 0
    assert output == expected