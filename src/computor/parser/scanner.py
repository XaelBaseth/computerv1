class Scanner:
	"""
	Sequential character reader for a string buffer.
	"""
	
	def __init__(self, buffer: str):
		if not isinstance(buffer, str):
			raise TypeError(f"Scanner buffer must be a string, got {type(buffer).__name__}")
		self.buffer = buffer
		self._cursor = 0

	def read(self):
		"""
		Return the next character from the buffer, or False if end is reached.
		"""
		if (self._cursor >= len(self.buffer)):
			return False

		char = self.buffer[self._cursor]
		self._cursor += 1
		return char

	@property
	def cursor(self):
		"""Current position in the buffer."""
		return self._cursor