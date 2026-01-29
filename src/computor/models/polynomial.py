from computor.math.sqrt import sqrt_newton
from computor.models.unknown import Unknown
from fractions import Fraction

class Polynomial:
	"""
	Represents a polynomial equation in reduced form.
	Stores coefficients for all degrees.
	"""
	
	def __init__(self, coefficients: dict[int, Unknown]):
		"""
		Args:
			coefficients: Dictionary mapping degree -> Unknown object
			Example: {0: Unknown(5, 0), 1: Unknown(-6, 1), 3: Unknown(-5.6, 3)}
		"""
		self.coefficients = coefficients
	
	def __str__(self) -> str:
		"""Returns the reduced form as a string including zero coefficients for missing degrees."""
		max_degree = self.get_degree()
		terms = []

		for degree in range(max_degree + 1):
			unknown = self.coefficients.get(degree, Unknown(0, degree))
			terms.append(f"{Unknown.fmt_coef(unknown.coef)} * X^{degree}")

		result = terms[0]
		for term in terms[1:]:
			if term.startswith("-"):
				result += f" - {term[1:]}"
			else:
				result += f" + {term}"

		return f"Reduced form: {result} = 0"
	
	def get_degree(self) -> int:
		"""Returns the highest degree with non-zero coefficient"""
		max_degree = 0
		for degree, unknown in self.coefficients.items():
			if unknown.coef != 0:
				max_degree = max(max_degree, degree)
		return max_degree
	
	def resolve(self):
		degree = self.get_degree()
		print(self)
		
		if degree == 0:
			c = self.coefficients.get(0, Unknown(0, 0))
			Polynomial.ResolveDefault(c)
		elif degree == 1:
			b = self.coefficients.get(1, Unknown(0, 1))
			c = self.coefficients.get(0, Unknown(0, 0))
			Polynomial.ResolveLinear(b, c)
		elif degree == 2:
			a = self.coefficients.get(2, Unknown(0, 2))
			b = self.coefficients.get(1, Unknown(0, 1))
			c = self.coefficients.get(0, Unknown(0, 0))
			Polynomial.ResolveQuadratic(a, b, c)
		else:
			print(f"Polynomial degree: {degree}")
			print("The polynomial degree is strictly greater than 2, I can't solve.")
	
	@staticmethod
	def ResolveDefault(c: Unknown):
		"""Resolve degree 0 : c = 0"""
		if c.coef == 0:
			print("Any real number is a solution.")
		else:
			print("No solution.")
	
	@staticmethod
	def ResolveLinear(b: Unknown, c: Unknown):
		"""Resolve degree 1 : bx + c = 0"""
		print("Polynomial degree: 1")
		
		if b.coef == 0:
			if c.coef == 0:
				print("Any real number is a solution.")
			else:
				print("No solution.")
			return
		
		solution = -c.coef / b.coef
		print("The solution is:")
		if solution.is_integer():
			print(int(solution))
		else:
			print(solution)

	@staticmethod
	def ResolveQuadratic(a: Unknown, b: Unknown, c: Unknown):
		"""Resolve degree 2: ax² + bx + c = 0"""
		print("Polynomial degree: 2")
		if a.coef == 0:
			return Polynomial.ResolveLinear(b, c)

		discriminant = b.coef ** 2 - 4 * a.coef * c.coef

		if discriminant > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			Polynomial.positive(discriminant, b, a)

		elif discriminant == 0:
			print("Discriminant is equal to zero, the solution is:")
			x = -b.coef / (2 * a.coef)
			print(f"{x:.6f}")

		else:
			print("Discriminant is strictly negative, the two complex solutions are:")
			Polynomial.negative(discriminant, b, a)
	
	@staticmethod
	def positive(discriminant, b, a):
		"""Calculate and print the two real solutions for positive discriminant."""
		sqrt_delta = sqrt_newton(discriminant)
		x1 = (-b.coef + sqrt_delta) / (2 * a.coef)
		x2 = (-b.coef - sqrt_delta) / (2 * a.coef)
		print(f"{x2:.6f}")
		print(f"{x1:.6f}")

	@staticmethod
	def negative(discriminant, b, a):
		"""Calculate and print the two complex solutions for negative discriminant."""
		real_num = int(-b.coef)
		real_den = int(2 * a.coef)
		real_frac = Fraction(real_num, real_den)

		sqrt_val = int(sqrt_newton(-discriminant))
		imag_num = sqrt_val
		imag_den = int(2 * a.coef)
		imag_frac = Fraction(imag_num, imag_den)

		if real_frac == 0:
			print(f"{imag_frac.numerator}i/{imag_frac.denominator}")
			print(f"-{imag_frac.numerator}i/{imag_frac.denominator}")
		else:
			if imag_frac.denominator == 1:
				print(f"{real_frac} + {imag_frac.numerator}i")
				print(f"{real_frac} - {imag_frac.numerator}i")
			else:
				print(f"{real_frac} + {imag_frac.numerator}i/{imag_frac.denominator}")
				print(f"{real_frac} - {imag_frac.numerator}i/{imag_frac.denominator}")