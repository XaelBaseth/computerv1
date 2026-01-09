class Token:
	"""
	Represents a token produced by the Lexer.
	"""
	def __init__(self, type: int):
		if type not in TOKEN_TYPE.values():
			raise ValueError(f"Invalid token type: {type}")
		self.type = type
		self._value = ''

	def __str__(self):
		"""String representation of the token's value."""
		return '{}'.format(self._value)

	def __add__(self, other):
		"""Concatenate a string to the token's value."""
		self._value = self._value + other
		return self

	def __eq__(self, other):
		"""Equality check with another token or string."""
		return self._value == other

	def __float__(self):
		"""Return the token's value as a float."""
		return float(self._value)

	def clone(self):
		"""Return a deep copy of the token."""
		token = Token(self.type)
		token._value = self._value
		return token

TOKEN_TYPE = {
"EOF": 0,
"Whitespace": 1,
"Symbol": 2,
"Number": 3,
"Unknown": 4,
}