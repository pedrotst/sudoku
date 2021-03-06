from square import Square, Square_Values

class Board(object):

	def __init__(self):
		self.board = [[Square(row, col) for col in range(9)] for row in range(9)]

	def __init__(self, matrix):
		self.board = [[Square(row, col) for col in range(9)] for row in range(9)]
		for row_num, row in enumerate(matrix):
			for col_num, ele in enumerate(row):
				if(ele in [str(x) for x in range(1,10)]):
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

	def __eq__(self, other):
		for row1, row2 in zip(self.board, other.board):
			for ele1, ele2 in zip(row1, row2):
				if ele1 != ele2:
					return False
		return True

	def get_board(self):
		return self.board

	def set_element(self, elem, row, col):
		self.board[row][col].set_possibility(elem, Square_Values.true)

	def get_row(self, row, col):
		'''I'll leave row and col so these functions can be used as checking_fun in
		self.check_only_possible'''
		return self.board[row]

	def get_col(self, row, col):
		'''Idem'''
		return [x[col] for x in self.board]

	def get_block(self, row, col, block = None):
		if block is None:
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

	def calc_adjacency(self, block):
		if block % 3 == 0:
			return 1, 2
		elif block % 3 == 1:
			return -1, 1
		else:
			return -1, -2

	def calc_below_above(self, block):
		if block < 3:
			return 3, 6
		elif 3 <= block < 6:
			return -3, 3
		else:
			return -3, -6

	def delete_spaces(self, _list):
		return [x for x in _list if repr(x) != '_']

	def get_only_possible(self, block, row_or_col, get_method):
		block_list = self.get_block(0, 0, block)
		row_block_list = [x for x in block_list if row_or_col == get_method(x)]
		group_imp_list = []
		for ele in block_list:
			if ele not in row_block_list:
				group_imp_list.append(set(ele.get_impossible_list()))

		if len(group_imp_list) != 0:
			inters_set = set.intersection(*group_imp_list)
		else:
			return []

		row_block_poss_list = []
		for ele in row_block_list:
			if not ele.is_set():
				row_block_poss_list.append(set(ele.get_possible_list()))
			
		if len(row_block_poss_list) != 0:
			inters_set2 = set.intersection(*row_block_poss_list)
		else:
			return []

		return list(set.intersection(inters_set2, inters_set))
		

	def impossible_list(self, row, col):
		row_list = self.get_row(row, 0)
		col_list = self.get_col(0, col)
		block_list = self.get_block(row,col)
		impossible_list = self.delete_spaces(row_list) + self.delete_spaces(col_list) + self.delete_spaces(block_list)
		impossible_list = [x for x in self.board[row][col].get_possible_list() if x in [repr(i) for i in impossible_list]]

		#this bit of code will find elements in the row which must be in another block
		block = self.calc_block(row, col)
		n1, n2 = self.calc_adjacency(block)
		imp_block1 = self.get_only_possible(block+n1, row, lambda x: x.get_row()) 
		imp_block2 = self.get_only_possible(block+n2, row, lambda x: x.get_row())

		#and this bit will find elements in the collumn which must be in another block
		n3, n4 = self.calc_below_above(block)
		imp_block3 = self.get_only_possible(block+n3, col, lambda x: x.get_col())
		imp_block4 = self.get_only_possible(block+n4, col, lambda x: x.get_col())

		impossible_list += imp_block1 + imp_block2 + imp_block3 + imp_block4
		
		return impossible_list

	def validate_element(self, row, col):
		impossible_list = self.impossible_list(row,col)
		for impossible_ele in impossible_list:
			self.board[row][col].set_possibility(impossible_ele, Square_Values.false)
	
	def check_only_possible(self, checking_fun, row, col):
		check_group = checking_fun(row,col)
		group_imp_list = []
		for ele in check_group:
			if(ele is not self.board[row][col]):
				group_imp_list.append(set(ele.get_impossible_list()))
		inters_list = set.intersection(*group_imp_list)
		
		for ele in check_group:
			if(repr(ele) in inters_list):
				inters_list.remove(repr(ele))
				
		inters_list = list(inters_list)
		if(len(inters_list) == 1):
			if(inters_list[0] not in self.impossible_list(row, col)):
				self.board[row][col].set_possibility(inters_list[0], Square_Values.true)

	def validate_board(self):

		for row_num, row in enumerate(self.board):
			for col_num, ele in enumerate(row):
				row_list = self.get_row(row_num, 0)
				col_list = self.get_col(0, col_num)
				block_list = self.get_block(row_num,col_num)
				if(self.has_repeated(row_list) or self.has_repeated(col_list) or self.has_repeated(block_list)):
					print(self)
					raise AttributeError("Elemento na row {} col {} está repetido".format(row_num, col_num))

	def has_repeated(self, _list):
		_list = [repr(x) for x in _list if repr(x) != '_']
		for x in _list:
			if(_list.count(x) > 1):
				return True
		return False


