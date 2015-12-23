from board import Board

def check_row(board):

	print(board.get_row(2))

def check_col(board):
	print(board.get_col(1))

def check_block(board):
	print(board.get_block(8))

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
	print(board)
	flag = True

	while(flag):
		flag = check_board
	check_block(board)

