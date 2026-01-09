from computor.parser.parser import Parser

def resolve(buffer: str):
	"""
	Docstring for resolve
	
	:param buffer: Description
	:type buffer: str
	"""
	try:
		parser = Parser(buffer)
		parser.parse()
	except KeyError as e:
		print("\n{error}".format(error=str(e)))
	except:
		return