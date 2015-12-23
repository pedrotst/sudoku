from square import Square, Square_Values

class Board(object):

	def __init__(self):
		self.board = [[Square() for _ in range(9)] for _ in range(9)]

	def __str__(self):
		string = ''
		for row_num, row in enumerate(self.board):
			if(row_num % 3 == 0):
				string += '=========================\n'
			for col_num, ele in enumerate(row):
				if(col_num % 3 == 0):
					string += '| '
				string += str(ele) + ' '
			string += '|\n'

		string += '=========================\n'
		return string

	def __repr__(self):
		return self.__str__()

	def get_board(self):
		return self.board

	def set_element(self, elem, row, col):
		self.board[row][col].set_possibility(elem, Square_Values.true)

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

	def calc_block(self, row, col):
		if 0 <= row < 3:
			if 0 <= col < 3:
				return 0
			elif 3 <= col < 6:
				return 1
			elif 6 <= col < 9:
				return 2
		elif 3 <= row < 6:
			if 0 <= col < 3:
				return 3
			elif 3 <= col < 6:
				return 4
			elif 6 <= col < 9:
				return 5
		elif 6 <= row < 9:
			if 0 <= col < 3:
				return 6
			elif 3 <= col < 6:
				return 7
			elif 6 <= col < 9:
				return 8

	def delete_spaces(self, _list):
		return [x for x in _list if str(x) != '_']

	def validate_element(self, row, col):
		row_list = self.get_row(row)
		print(self.delete_spaces(row_list))
		col_list = self.get_col(col)
		print(self.delete_spaces(col_list))
		block_list = self.get_block(self.calc_block(row,col))
		print(self.delete_spaces(block_list))
		print(self.board[row][col].get_possible_list())