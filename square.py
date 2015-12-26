from enum import Enum

class Square_Values(Enum):
	true = 1
	false = -1
	maybe = 0

class Square(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col
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

	def get_row_col(self):
		return self.row, self.col

	def validate(self):
		true_count = 0
		maybe_count = 0
		for x in self.square:
			if(self.square[x] == Square_Values.true):
				true_count += 1
			elif(self.square[x] == Square_Values.maybe):
				maybe_count += 1
				maybe_num = x
		if(maybe_count == 1):
			for k in self.square:
				self.square[k] = Square_Values.false
			self.square[maybe_num] = Square_Values.true


		if(true_count > 1):
			raise AttributeError("A square {},{} tem mais de um valor possível!".format(self.row, self.col))

	def set_possibility(self, key, value):
		self.validate() 
		if value == Square_Values.true:
			for k in self.square:
				self.square[k] = Square_Values.false
		self.square[key] = value

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

	def get_impossible_list(self):
		
		impossible_list = []
		if not self.is_set():
			for key in self.square:
				if self.square[key] == Square_Values.false:
					impossible_list.append(key)
		return impossible_list

	def is_equal(self, compare_with):
		for x1, x2 in zip(self.square, compare_with.square):
			if self.square[x1] !=  compare_with.square[x2]:
				return False
		return True