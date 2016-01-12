from board import Board

board4 = Board([
	['9', ' ', '6', ' ', '1', '3', ' ', ' ', '8'],
	[' ', '5', '8', ' ', ' ', ' ', ' ', '9', ' '],
	[' ', '3', ' ', ' ', ' ', ' ', ' ', '1', ' '],
	[' ', '6', ' ', '8', ' ', ' ', '9', '2', ' '],
	[' ', ' ', '3', '4', ' ', '9', '1', ' ', ' '],
	[' ', '4', '9', ' ', ' ', '6', ' ', '3', ' '],
	[' ', '9', ' ', ' ', ' ', ' ', ' ', '8', ' '],
	[' ', '1', ' ', ' ', ' ', ' ', '6', '7', ' '],
	['4', ' ', ' ', '9', '6', ' ', '3', ' ', '1']])	
board3 = Board([
	[' ', ' ', ' ', ' ', '3', '7', '6', ' ', ' '],
	[' ', ' ', ' ', '6', ' ', ' ', ' ', '9', ' '],
	[' ', ' ', '8', ' ', ' ', ' ', '7', ' ', '4'],
	[' ', '9', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
	['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '9'],
	['3', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' '],
	['7', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' '],
	[' ', '1', ' ', ' ', '2', ' ', ' ', ' ', ' '],
	[' ', ' ', '2', '5', '4', ' ', ' ', '6', ' ']])	
ex_board = Board([
	[' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' '],
	[' ', ' ', ' ', '6', '9', '5', ' ', ' ', ' '],
	[' ', ' ', ' ', '4', '7', '8', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', '3', '4', ' ', ' ', ' '],
	[' ', ' ', ' ', '7', '8', '9', ' ', ' ', ' '],
	[' ', ' ', ' ', '5', ' ', '6', ' ', ' ', ' '],
	[' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
	['2', '3', '4', ' ', ' ', ' ', ' ', ' ', ' ']])	
blank_board = Board([
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])	
induction_ex = Board([
	[' ', '3', ' ', ' ', ' ', '4', ' ', '8', '7'],
	['9', '4', '8', '7', ' ', ' ', '5', ' ', ' '],
	[' ', '6', ' ', '8', ' ', ' ', ' ', ' ', '9'],
	[' ', '1', ' ', '5', '8', '6', '7', '2', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', '8', '7', '3', '1', '2', ' ', '5', ' '],
	['8', ' ', ' ', ' ', ' ', '3', ' ', '7', ' '],
	[' ', ' ', '3', ' ', ' ', '7', '8', '6', '5'],
	['5', '7', ' ', '2', ' ', ' ', ' ', '9', ' ']])	
board1 = Board([
	['8 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
	[' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
	[' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
	[' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
	[' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
	[' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
	[' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' ']])
board = Board([[' '*9]*9])
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

board.set_element('5', 0, 1)
board.set_element('2', 0, 2)
board.set_element('6', 0, 5)
board.set_element('1', 1, 0)
board.set_element('6', 1, 1)
board.set_element('9', 1, 3)
board.set_element('4', 1, 8)
board.set_element('4', 2, 1)
board.set_element('9', 2, 2)
board.set_element('8', 2, 3)
board.set_element('3', 2, 5)
board.set_element('6', 2, 6)
board.set_element('2', 2, 7)
board.set_element('4', 3, 0)
board.set_element('8', 3, 6)
board.set_element('8', 4, 1)
board.set_element('3', 4, 2)
board.set_element('2', 4, 3)
board.set_element('1', 4, 5)
board.set_element('5', 4, 6)
board.set_element('9', 4, 7)
board.set_element('1', 5, 2)
board.set_element('2', 5, 8)
board.set_element('9', 6, 1)
board.set_element('7', 6, 2)
board.set_element('3', 6, 3)
board.set_element('5', 6, 5)
board.set_element('2', 6, 6)
board.set_element('4', 6, 7)
board.set_element('2', 7, 0)
board.set_element('9', 7, 5)
board.set_element('5', 7, 7)
board.set_element('6', 7, 8)
board.set_element('1', 8, 3)
board.set_element('9', 8, 6)
board.set_element('7', 8, 7)
