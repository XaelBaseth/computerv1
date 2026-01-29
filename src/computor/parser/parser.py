from computor.models.unknown import Unknown
from computor.models.polynomial import Polynomial
from computor.parser.lexer import Lexer
from computor.parser.token import TOKEN_TYPE

class Parser:
	"""
	Syntax parser for polynomial equations of degree ≤ 2.

	This parser consumes tokens produced by a Lexer and builds a polynomial
	representation of an equation of the form:

		ax^2 + bx + c = 0

	The input expression may contain a left-hand side (LHS) and a right-hand
	side (RHS). Terms on the RHS are algebraically moved to the LHS by applying
	a sign inversion during parsing.

	The parser accumulates coefficients for degrees 2, 1, and 0 into
	Unknown objects, then constructs a Polynomial instance and resolves it.

	Invalid syntax, unsupported operators, or malformed expressions
	raise a KeyError via the lexer.
	"""
			
	def __init__(self, buffer: str):
		self._lexer = Lexer(buffer)
		self._token = self._lexer.lexer(True)
		self._a = Unknown(0, 2)
		self._b = Unknown(0, 1)
		self._c = Unknown(0, 0)

	def _get_sign_multiplier(self, rhs):
		"""Returns coefficient multiplier: 1 for LHS, -1 for RHS"""
		return -1 if rhs else 1

	def _handle_signed_token(self, rhs):
		"""Parse next token after +/- operator"""
		self._token = self._lexer.lexer(True)

		if self._token.type == TOKEN_TYPE['Number']:
			self.parse_number(rhs)
		elif self._token.type == TOKEN_TYPE['Unknown']:
			coef = self._get_sign_multiplier(rhs)
			self.parse_unknown(coef)
		else:
			self._lexer.raise_KeyError()

	def _process_token(self, rhs):
		"""Process current token based on its type"""
		if self._token.type == TOKEN_TYPE['EOF']:
			self._lexer.raise_KeyError()
		elif self._token.type == TOKEN_TYPE['Unknown']:
			self.parse_unknown(self._get_sign_multiplier(rhs))
		elif self._token.type == TOKEN_TYPE['Number']:
			self.parse_number(rhs)
		elif self._token == '-':
			self._handle_signed_token(not rhs)
		elif self._token == '+':
			self._handle_signed_token(rhs)
		elif self._token.type == TOKEN_TYPE['Symbol']:
			if self._token in ('/', '*', '^'):
				self._lexer.raise_KeyError()
		else:
			self._token = self._lexer.lexer(True)

	def parse(self):
		rhs = False
		
		while self._token.type != TOKEN_TYPE['EOF']:
			while (not rhs and self._token != '=') or (rhs and self._token.type != TOKEN_TYPE['EOF']):
				self._process_token(rhs)

			if self._token == '=':
				rhs = True
				self._token = self._lexer.lexer(True)
				if self._token.type == TOKEN_TYPE['EOF']:
					self._lexer.raise_KeyError()
		
		if not hasattr(self, '_coefficients'):
			self._coefficients = {0: Unknown(0, 0)}
		else:
			if 0 not in self._coefficients:
				self._coefficients[0] = Unknown(0, 0)

		poly = Polynomial(self._coefficients)
		poly.resolve()

	def parse_number(self, negative):
		coef = float(self._token) if not negative else -1 * float(self._token)
		self._token = self._lexer.lexer(True)

		if self._token.type == TOKEN_TYPE['Unknown']:
			return self.parse_unknown(coef)
		elif self._token.type == TOKEN_TYPE['Symbol']:
			if self._token == '*':
				self._token = self._lexer.lexer(True)
				if self._token.type != TOKEN_TYPE['Unknown']:
					self._lexer.raise_KeyError()
				return self.parse_unknown(coef)

		if not hasattr(self, '_coefficients'):
			self._coefficients = {}
		if 0 not in self._coefficients:
			self._coefficients[0] = Unknown(0, 0)

		self._coefficients[0] = self._coefficients[0] + coef

	def parse_unknown(self, coef):
		unknown = Unknown(coef, 1)
		self._token = self._lexer.lexer(True)

		if self._token == '^':
			self._token = self._lexer.lexer(True)
			if self._token.type != TOKEN_TYPE['Number']:
				self._lexer.raise_KeyError()
			unknown.degree = float(self._token)
			if not unknown.degree.is_integer():
				self._lexer.raise_KeyError()
			self._token = self._lexer.lexer(True)

		degree = int(unknown.degree)

		if not hasattr(self, '_coefficients'):
			self._coefficients = {}
		if degree not in self._coefficients:
			self._coefficients[degree] = Unknown(0, degree)
		
		self._coefficients[degree] = self._coefficients[degree] + unknown