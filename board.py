class Board(object):

	def __init__(self):
		self.board = [['_' for _ in range(9)] for _ in range(9)]

	def __str__(self):
		string = ''
		for row_num, row in enumerate(self.board):
			if(row_num % 3 == 0):
				string += '=========================\n'
			for col_num, ele in enumerate(row):
				if(col_num % 3 == 0):
					string += '| '
				string += ele + ' '
			string += '|\n'

		string += '=========================\n'
		return string

	def __repr__(self):
		return self.__str__()
