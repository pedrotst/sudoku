from square import Square, Square_Values

class Board(object):

	def __init__(self):
		self.board = [[Square(row, col) for col in range(9)] for row in range(9)]

	def __init__(self, matrix):
		self.board = [[Square(row, col) for col in range(9)] for row in range(9)]
		for row_num, row in enumerate(matrix):
			for col_num, ele in enumerate(row):
				if(ele in [str(x) for x in range(10)]):
					self.board[row_num][col_num].set_possibility(ele, Square_Values.true)

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

	def get_row(self, row, col):
		return self.board[row]

	def get_col(self, row, col):
		return [x[col] for x in self.board]

	def get_block(self, row, col):
		block = self.calc_block(row, col)
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
		return [x for x in _list if repr(x) != '_']

	def impossible_list(self, row, col):
		row_list = self.get_row(row, 0)
		col_list = self.get_col(0, col)
		block_list = self.get_block(row,col)
		impossible_list = self.delete_spaces(row_list) + self.delete_spaces(col_list) + self.delete_spaces(block_list)
		impossible_list = [x for x in self.board[row][col].get_possible_list() if x in [repr(i) for i in impossible_list]]
		return impossible_list

	def validate_element(self, row, col):
		impossible_list = self.impossible_list(row,col)
		# print("row: {}, col: {}, imp_list: {}".format(row, col, impossible_list))
		for impossible_ele in impossible_list:
			self.board[row][col].set_possibility(impossible_ele, Square_Values.false)
	
	def check_only_possible(self, checking_fun, row, col):
		check_group = checking_fun(row,col)
		group_imp_list = []
		for ele in check_group:
			if(ele is not self.board[row][col]):
				group_imp_list.append(set(ele.get_impossible_list()))
				if(row == 3 and col == 2):
					print("Ele: {}, Row: {}, Col: {}, imp_list: {}:".format(ele, ele.row, ele.col, sorted(ele.get_impossible_list())))
		# print(row, col, group_imp_list, check_group)
		inters_list = set.intersection(*group_imp_list)
		
		for ele in check_group:
			if(repr(ele) in inters_list):
				inters_list.remove(repr(ele))
		inters_list = list(inters_list)
		# if (3 <= row < 6 and 0 <= col < 3):
		if(len(inters_list) == 1):
			self.board[row][col].set_possibility(inters_list[0], Square_Values.true)

	def is_equal(self, compare_with):
		for row1, row2 in zip(self.board, compare_with):
			for ele1, ele2 in zip(row1, row2):
				if not ele1.is_equal(ele2):
					return False
		return True