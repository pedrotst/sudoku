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

	def set_element(self, elem, row, col):
		self.board[row][col] = elem

	def get_row(self, row):
		return self.board[row]

	def get_col(self, col):
		return [x[col] for x in self.board]

	def get_block(self, block):
		block_list = []
		if(block == 0):
			for not_merged in [x[:3] for x in self.board[:3]]:
				block_list += not_merged
		elif(block == 1):
			for not_merged in [x[3:6] for x in self.board[:3]]:
				block_list += not_merged
		elif(block == 2):
			for not_merged in [x[6:9] for x in self.board[:3]]:
				block_list += not_merged
		elif(block == 3):
			for not_merged in [x[:3] for x in self.board[3:6]]:
				block_list += not_merged
		elif(block == 4):
			for not_merged in [x[3:6] for x in self.board[3:6]]:
				block_list += not_merged
		elif(block == 5):
			for not_merged in [x[6:9] for x in self.board[3:6]]:
				block_list += not_merged
		elif(block == 6):
			for not_merged in [x[:3] for x in self.board[6:9]]:
				block_list += not_merged
		elif(block == 7):
			for not_merged in [x[3:6] for x in self.board[6:9]]:
				block_list += not_merged
		elif(block == 8):
			for not_merged in [x[6:9] for x in self.board[6:9]]:
				block_list += not_merged

		return block_list