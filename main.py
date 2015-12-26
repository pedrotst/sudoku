from board import Board



if __name__ == '__main__':
	board = Board()
	board.set_element('2', 0, 1)
	board.set_element('5', 1, 1)
	board.set_element('4', 2, 1)
	board.set_element('7', 1, 5)
	board.set_element('6', 2, 4)
	board.set_element('8', 2, 5)
	board.set_element('1', 0, 8)
	board.set_element('5', 2, 8)
	board.set_element('7', 3, 1)
	board.set_element('1', 3, 6)
	board.set_element('3', 3, 8)
	board.set_element('9', 4, 2)
	board.set_element('7', 4, 3)
	board.set_element('4', 5, 0)
	board.set_element('3', 5, 3)
	board.set_element('8', 5, 4)
	board.set_element('7', 5, 7)
	board.set_element('9', 5, 8)
	board.set_element('6', 6, 0)
	board.set_element('1', 6, 3)
	board.set_element('9', 6, 8)
	board.set_element('3', 7, 0)
	board.set_element('2', 7, 2)
	board.set_element('7', 7, 4)
	board.set_element('5', 7, 5)
	board.set_element('6', 7, 6)
	board.set_element('4', 8, 2)
	board.set_element('3', 8, 5)
	# board.set_element('1', 0, 0)
	# board.set_element('2', 0, 1)
	# board.set_element('3', 0, 2)
	# board.set_element('4', 0, 3)
	# board.set_element('5', 0, 4)
	# board.set_element('6', 0, 5)
	# board.set_element('7', 0, 6)
	# board.set_element('8', 0, 7)
	print(board)

	flag = True

	
	old_board = Board()
	while(not board.is_equal(old_board.get_board())):	
		old_board = board
		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.validate_element(row_num, col_num)
		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.check_only_possible(board.get_block, row_num, col_num)
					board.check_only_possible(board.get_col, row_num, col_num)
					board.check_only_possible(board.get_row, row_num, col_num)
				# print(.get_possible_list())

	# board.check_only_possible(board.get_block, 3, 0)	
	# board.validate_element(0, 0)
	# print(board.get_board()[0][8].get_possible_list())
	print(board)
def check_row(board, row):
	print(board.get_row(row))

def check_col(board, col):
	print(board.get_col(col))

def check_block(board, block):
	print(board.get_block(block))