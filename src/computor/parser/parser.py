from computor.models.unknown import Unknown
from computor.models.polynomial import Polynomial
from computor.parser.lexer import Lexer
from computor.parser.token import TOKEN_TYPE, Token

class Parser:
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

		poly = Polynomial(self._a, self._b, self._c)
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

		self._c = self._c + coef

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

		if unknown.degree == 2:
			self._a = self._a + unknown
		elif unknown.degree == 1:
			self._b = self._b + unknown
		elif unknown.degree == 0:
			self._c = self._c + unknown
		else:
			print("The polynomial degree is stricly greater than 2, I can't solve.")
			raise Exception()