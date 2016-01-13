import exemplos
import copy


if __name__ == '__main__':
	board = exemplos.induction_ex
	print(board)

	board.validate_board()
	
	
	old_board = exemplos.blank_board
	while(board != old_board):
		old_board = copy.deepcopy(board)

		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.validate_element(row_num, col_num)
		
		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.check_only_possible(board.get_block, row_num, col_num)


		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.validate_element(row_num, col_num)


		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.check_only_possible(board.get_col, row_num, col_num)


		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.validate_element(row_num, col_num)


		for row_num, row in enumerate(board.get_board()):
			for col_num, ele in enumerate(row):
				if(not ele.is_set()):
					board.check_only_possible(board.get_row, row_num, col_num)
				# print(.get_possible_list())
		board.validate_board()
		print(board)
	# board.check_only_possible(board.get_block, 3, 0)	
	# board.validate_element(0, 0)
	# print(board.get_board()[0][8].get_possible_list())
def check_row(board, row):
	print(board.get_row(row))

def check_col(board, col):
	print(board.get_col(col))

def check_block(board, block):
	print(board.get_block(block))
