def sqrt_newton(w, precision=0.01) -> float:
	"""
	Compute the square root of a positive number using Newton's method.

	This function approximates sqrt(w) by iteratively refining a guess g.
	Newton's method is applied to the equation g^2 - w - 0, which leads to the update rule:

		g_next = (g + w / g) / 2

	The iteration stops when the relative difference between two consecutive guesses is smaller than the given precision.

	:param w (float): Number whose square root is computed. Must be >= 0.
	:param precision (float): Relative error tolerance for convergence.

	:returns (float):  an appoximation of sqrt(w)
	:raises (ValueError):  if w is negative
	"""
	if w == 0:
		return 0.0
    
	if w < 0:
		raise ValueError("sqrt undefined for negative numbers")

	g = 1.0
	while True:
		new_g = (g + w / g) / 2
		if abs(new_g - g) < precision * g:
			return new_g
		g = new_g