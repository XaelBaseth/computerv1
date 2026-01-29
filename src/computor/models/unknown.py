class Unknown:
	"""
	Represents a single polynomial of the form : coef * x^degree

	Provides basic arithmetic operations with scalars, string representation
	and comparison based on the coefficient value. Used for constructing
	and manipulating polynomials term by term.
	"""

	def __init__(self, coef: float, degree: int):
		self.coef = float(coef)
		self.degree = degree
	
	def __str__(self) -> str:
		"""
		Returns a human-readable string representation of the term.
		"""
		if self.coef == 0:
			return ""

		if self.degree == 0:
			return str(int(self.coef)) if self.coef.is_integer() else str(self.coef)

		coef_str = "" if self.coef == 1 else (str(int(self.coef)) if self.coef.is_integer() else str(self.coef))
		if self.degree == 1:
			return f"{coef_str}x"
		elif self.degree == 2:
			return f"{coef_str}x²"
		else:
			return f"{coef_str}x^{self.degree}"

	def fmt_coef(x: float) -> str:
		"""
		Formats the coefficient for display, removing unnecessary decimal points.
		"""
		if x.is_integer():
			return str(int(x))
		return str(x)
	
	def __repr__(self) -> str:
		"""
		Returns a detailed string representation for debugging.
		"""
		return f"Unknown({self.coef}, {self.degree})"
	
	def __float__(self) -> float:
		"""
		Converts the term to its coefficient as a float.
		"""
		return self.coef
	
	def __neg__(self):
		"""
		Returns the negation of the term.
		"""
		return Unknown(-self.coef, self.degree)

	def _operate(self, other, op):
		"""
		Helper method to apply arithmetic operations with scalars.
		"""
		return Unknown(op(self.coef, other), self.degree)
	
	def __add__(self, other):
		"""
		 Adds a scalar to the term's coefficient.
		"""
		return self._operate(other, lambda a, b: a + b)
	
	def __radd__(self, other):
		"""
		Adds the term's coefficient to a scalar (right-hand addition).
		"""
		return self._operate(other, lambda a, b: b + a)
	
	def __sub__(self, other):
		"""
		Subtracts a scalar from the term's coefficient.
		"""
		return self._operate(other, lambda a, b: a - b)
	
	def __rsub__(self, other):
		"""
		Subtracts the term's coefficient from a scalar (right-hand subtraction).
		"""
		return self._operate(other, lambda a, b: b - a)
	
	def __mul__(self, other):
		"""
		Multiplies the term's coefficient by a scalar.
		"""
		return self._operate(other, lambda a, b: a * b)
	
	def __rmul__(self, other):
		"""
		Multiplies a scalar by the term's coefficient (right-hand multiplication).
		"""
		return self._operate(other, lambda a, b: b * a)
	
	def __truediv__(self, other):
		"""
		Divides the term's coefficient by a scalar.
		"""
		return self._operate(other, lambda a, b: a / b)
	
	def __eq__(self, other):
		"""
		Compares the term's coefficient for equality with a scalar.
		"""
		return self.coef == other
	
	def __lt__(self, other):
		"""
		Checks if the term's coefficient is less than a scalar.
		"""
		return self.coef < other
	
	def __gt__(self, other):
		"""
		Checks if the term's coefficient is greater than a scalar.
		"""
		return self.coef > other