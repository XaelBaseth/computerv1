from computor.math.sqrt import sqrt_newton
from computor.models.unknown import Unknown

class Polynomial:
	"""
	Represents a polynomial equation in reduced form.
	Stores coefficients as Unknown objects for degrees 0, 1, and 2.
	"""
	def __init__(self, a: Unknown, b: Unknown, c: Unknown):
		self.a = a
		self.b = b
		self.c = c 
	
	def __str__(self) -> str:
		"""Returns the reduced form as a string"""
		terms = []
		
		if self.c.coef != 0 or (self.a.coef == 0 and self.b.coef == 0):
			terms.append(f"{self.c.coef} * X^0")
		if self.b.coef != 0:
			terms.append(f"{self.b.coef} * X^1")
		if self.a.coef != 0:
			terms.append(f"{self.a.coef} * X^2")

		result = terms[0]
		for term in terms[1:]:
			if term.startswith("-"):
				result += f" - {term[1:]}"
			else:
				result += f" + {term}"

		return f"Reduced form: {result} = 0"
	
	def get_degree(self) -> int:
		"""Returns the degree of the polynomial"""
		if self.a.coef != 0:
			return 2
		elif self.b.coef != 0:
			return 1
		else:
			return 0
	
	def resolve(self):
		degree = self.get_degree()
		print(self)
		
		if degree == 0:
			Polynomial.ResolveDefault(self.c)
		elif degree == 1:
			Polynomial.ResolveLinear(self.b, self.c)
		elif degree == 2:
			Polynomial.ResolveQuadratic(self.a, self.b, self.c)
		else:
			print(f"Polynomial degree: {degree}")
			print("The polynomial degree is strictly greater than 2, I can't solve.")
	
	@staticmethod
	def ResolveDefault(c: Unknown):
		"""Resolve degree 0 : c = 0"""
		print("Polynomial degree: 0")
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
		print(f"{solution:.6f}")
	
	@staticmethod
	def ResolveQuadratic(a: Unknown, b: Unknown, c: Unknown):
		"""Resolve degree  2 : ax² + bx + c = 0"""
		print("Polynomial degree: 2")
		if a.coef == 0:
			return Polynomial.ResolveLinear(b, c)
		
		discriminant = b.coef ** 2 - 4 * a.coef * c.coef
		
		if discriminant > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			sqrt_delta = sqrt_newton(discriminant)
			x1 = (-b.coef + sqrt_delta) / (2 * a.coef)
			x2 = (-b.coef - sqrt_delta) / (2 * a.coef)
			print(f"{x2:.6f}")
			print(f"{x1:.6f}")
		
		elif discriminant == 0:
			print("Discriminant is equal to zero, the solution is:")
			x = -b.coef / (2 * a.coef)
			print(f"{x:.6f}")
		
		else:
			print("Discriminant is strictly negative, the two complex solutions are:")
			real_part = -b.coef / (2 * a.coef)
			imag_part = sqrt_newton(-discriminant) / (2 * a.coef)
			print(f"{real_part:.6f} + {imag_part:.6f}i")
			print(f"{real_part:.6f} - {imag_part:.6f}i")
