from enum import Enum

class Square_Values(Enum):
	true = 1
	false = -1
	maybe = 0

class Square(object):
	def __init__(self):
		self.square =  {'1': Square_Values.maybe,
						'2': Square_Values.maybe,
						'3': Square_Values.maybe,
						'4': Square_Values.maybe,
						'5': Square_Values.maybe,
						'6': Square_Values.maybe,
						'7': Square_Values.maybe,
						'8': Square_Values.maybe,
						'9': Square_Values.maybe}


	def __str__(self):
		self.validate()
		for x in self.square:
			if(self.square[x] == Square_Values.true):
				return x 
		return '_'
		
	def __repr__(self):
		return self.__str__()

	def validate(self):
		value = 0
		for x in self.square:
			if(x == Square_Values.true):
				x += 1
		if(value > 1):
			raise AttributeError("A square tem mais de um valor possível!")

	def set_possibility(self, key, value):
		self.square[key] = value
		self.validate()

	def is_set(self):
		if(repr(self) == '_'):
			return False
		return True

	def get_possible_list(self):
		possible_list = []
		if not self.is_set():
			for key in self.square:
				if self.square[key] == Square_Values.maybe:
					possible_list.append(key)
		return possible_list