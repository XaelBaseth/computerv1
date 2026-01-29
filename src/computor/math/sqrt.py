def sqrt_newton(nbr, precision=0.01) -> float:
	"""
	Compute the square root of a positive number using Newton's method.

	This function approximates sqrt(nbr) by iteratively refining a guess g.
	Newton's method is applied to the equation g^2 - nbr - 0, which leads to the update rule:

		g_next = (g + w / g) / 2

	The iteration stops when the relative difference between two consecutive guesses is smaller than the given precision.

	:param nbr (float): Number whose square root is computed. Must be >= 0.
	:param precision (float): Relative error tolerance for convergence.

	:returns (float):  an appoximation of sqrt(nbr)
	:raises (ValueError):  if nbr is negative
	"""
	if nbr == 0:
		return 0.0
    
	if nbr < 0:
		raise ValueError("sqrt undefined for negative numbers")

	g = 1.0
	while True:
		new_g = (g + nbr / g) / 2
		if abs(new_g - g) < precision * g:
			return new_g
		g = new_g