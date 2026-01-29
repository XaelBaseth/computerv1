from computor.parser.scanner import Scanner
from computor.parser.token import Token, TOKEN_TYPE

WHITESPACE_CHARS = "\t\n\v\f\r "
SYMBOL_CHARS = "+-=^*/"
DECIMAL_CHAR = '.'
NUMBER_CHARS = "0123456789"
UNKNOWN_CHARS = "Xx"

class Lexer:
	"""
	Lexical analyzer that converts an input character stream into tokens.

	This lexer reads characters sequentially from a Scanner and groups them
	into Token objects according to predefined character classes
	(whitespace, symbols, numbers, unknown identifiers).

	Supported token types:
	- Whitespace
	- Symbol
	- Number (integer and decimal, including forms like ".5")
	- Unknown (single-character identifiers such as 'X' or 'x')
	- EOF

	Invalid characters or malformed numbers (e.g. multiple decimal points)
	raise a KeyError with position information.
	"""
	
	def __init__(self, buffer):
		self._scan = Scanner(buffer)
		self._char = self._scan.read()
		self._token = Token(TOKEN_TYPE['Whitespace'])

	def lexer(self, no_whitespace=False):
			"""Return the next token"""
			while True:
				if not self._char:
					self._token = Token(TOKEN_TYPE['EOF'])
				elif self._char in WHITESPACE_CHARS:
					self.whitespace_token()
				elif self._char in SYMBOL_CHARS:
					self.symbol_token()
				elif self._char in NUMBER_CHARS or self._char == DECIMAL_CHAR:
					self.number_token()
				elif self._char in UNKNOWN_CHARS:
					self.unknown_token()
				else:
					self.raise_KeyError()

				if no_whitespace and self._token.type == TOKEN_TYPE['Whitespace']:
					continue
				break

			return self._token

	def raise_KeyError(self):
		"""Exception KeyError with clear message"""
		raise KeyError(
			f"Unknown symbol '{self._token._value}' at index {self._scan.cursor}"
		)

	def whitespace_token(self):
		"""Set Whitespace Token"""
		token = Token(TOKEN_TYPE['Whitespace'])
		while self._char in WHITESPACE_CHARS:
			token = token + self._char
			self._char = self._scan.read()
		
		self._token = token

	def symbol_token(self):
		"""Set Symbol Token"""
		token = Token(TOKEN_TYPE['Symbol'])
		token = token + self._char
		self._char = self._scan.read()
		self._token = token

	def number_token(self):
		"""Set number token (supports .5 or 0.5)"""
		token = Token(TOKEN_TYPE["Number"])
		has_decimal = False

		if self._char == DECIMAL_CHAR:
			token += '0'
			token += self._char
			has_decimal = True
			self._char = self._scan.read()

		while self._char and (self._char in NUMBER_CHARS or self._char == DECIMAL_CHAR):
			if self._char == DECIMAL_CHAR:
				if has_decimal:
					self.raise_KeyError()
				has_decimal = True
			token += self._char
			self._char = self._scan.read()

		self._token = token

	def unknown_token(self):
		"""Set Unknown Token"""
		token = Token(TOKEN_TYPE["Unknown"])
		token = token + self._char
		self._char = self._scan.read()
		self._token = token