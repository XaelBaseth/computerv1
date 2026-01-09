import math
import pytest
from computor.math.sqrt import sqrt_newton

def test_perfect_squares():
	assert sqrt_newton(1) == pytest.approx(1.0, rel=1e-2)
	assert sqrt_newton(4) == pytest.approx(2.0, rel=1e-2)
	assert sqrt_newton(16) == pytest.approx(4.0, rel=1e-2)
	assert sqrt_newton(25) == pytest.approx(5.0, rel=1e-2)
	assert sqrt_newton(25) == pytest.approx(5.0, rel=1e-2)

def test_zero():
	assert sqrt_newton(0) == 0.0

@pytest.mark.parametrize("value", [
	0.1, 0.5,
	2.0, 10.0,
	42.42, 123.456,
])
def test_against_math_sqrt(value):
	assert sqrt_newton(value) == pytest.approx(
		math.sqrt(value),
		rel=1e-2
	)

def test_custom_precision():
	value = 50.0
	precision = 1e-4
	result = sqrt_newton(value, precision=precision)

	reference = math.sqrt(value)
	relative_error = abs(result - reference) / reference
	assert relative_error < precision

def test_negative_value_raises():
	with pytest.raises(ValueError):
		sqrt_newton(-1)

def test_large_numbers_against_math():
	large_values = [
		10**12 + 123,
		10**15 + 42,
		10**18 + 987654,
	]

	for v in large_values:
		assert sqrt_newton(v) == pytest.approx(math.sqrt(v), rel=1e-2)