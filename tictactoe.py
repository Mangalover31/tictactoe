# Code outline:
# 1. Keep track of state of game -->
#   Keep track of what is happening in every box:
#     Keep track of boxes in 3 by 3 grid
#     Each box could be _ , O , or X
# 2. Make a move -->
#   Ask a player for coordinate for move
#   Player needs to be able to answer (needs to be able to give program coordinates)
#   Print the state of board before making move (optional)
#   If empty:
#    draw X or O at player coordinate based on which player they are
#   If not empty:
#     yell at them and ask for a proper move
# 3. Figure out if game is over:
# Maybe somebody won:
#   3 in a row of either X or O:
#     end it and say you won to whoever won
# Maybe its a draw:
#   No moves left and no one has three in a row:
#     end it and say its a draw
#
# 1.
#
# [[     ]
#  [     ]
#  [     ]]
#
#  _ X O
#  X _ O
#  _ _ _
#
#  2.
#
#  Hi player give me a move!
#
#  Player 1: here is a row: 2
#            here is a col: 1
#
# if array[row = 2][col = 1] is EMPTY and INBOUNDS:
#   figure out if player is X or O
#   array[row = 2][col = 1] = X or O
#
# 3. Figure out if game is over (after move 6), or every time if we are lazy
#
# Someone wins: someone has 3 in a row -->
#
# Check every row and see if a row has all X's or all O's
#             col
#             diag
#
# Every box filled --> draw
#
# Variables:
#
# grid
# whose_turn it is (player 1 or player 2)
# move_coordinate
#
# Functions:
# initialize_game(grid, whose_turn) --> fill grid with '_' and set whose_turn to True
# get_move(whose_turn) --> get move from a player and read it in and return it in proper representation
# is_move_valid(grid, coordinate) --> True or False if it is valid
# make_move(move_coordinate, whose_turn, grid) --> update grid
# get_game_status(grid) --> did someone win?, did someone draw?, or is game not over at all
# print_grid(grid) --> prints current game state
# play_game()
#
# Pseudocode:
#
# Variables:
#
# grid --> 3 x 3 2D array with elements that are 'X', 'O', '_'
# whose_turn --> boolean (is it X's turn or not X's turn)
#   True --> X's turn
#   False --> Os turn
# move_coordinate --> (row, col) both of these will integers
#
# Functions:
#
# make_move(move_coordinate, whose_turn, grid):
#
#   # Making sure we have a valid move
#   valid = is_move_valid(grid, move_coordinate)
#
#   while valid is False:
#     yell at them
#     new_coor = get_move(whose_turn)
#     valid = is_move_valid(grid, new_coor)
#
#   # Now we know that we have a valid move
#
#   # Making our valid move
#   if whose_turn is True:
#     grid[move_coordinate_row, move_coordinate_col] = 'X'
#   else:
#     grid[move_coordinate_row, move_coordinate_col] = 'O'
#
# is_move_valid(grid, coordinate):
#   # Check if the coordinate is in bounds
#   # Row and columns need to be both in the interval (0, 3]
#   (row, col)
#   if NOT (row > 0 and row <= 3 and col > 0 and col <= 3):
#     return False
#
#   # We only get here if the move is in bounds so now we need
#   # to see if the coordinate in the grid is empty
#   if grid[row][col] is '_':
#     return True
#   else:
#     return False
#
# get_move(whose_turn):
#   if whose_turn:
#     print "Hi player X please type a move"
#   else:
#     print "Hi player O please type a move"
#
#   wait until player prints something (example input could be 3 4)
#   convert this into (row, col) format (example could be (3, 4)  )
#   return (row, col)
#
# check_if_board_full(grid):
#
#   for row in grid:
#     for col in grid[row]:
#       if grid[row][col] == '_':
#         return False
#
#   return True
#
# get_game_status(grid):
#   if check_if_board_full(grid) is True:
#     return DRAW
#
#   X_win = ['X', 'X', 'X']
#   O_win = ['O', 'O', 'O']
#
#   # Check rows
#   for row in grid:
#     if grid[row] == X_win:
#       return X_WON
#     elif grid[row] = O_win:
#       return O_WON
#
#   # Check columns
#   for col in grid:
#     if grid[col] == X_win:
#       return X_WON
#     elif grid[col] = O_win:
#       return O_WON
#
#   # Check diagonals
#   diag_1_vals = []
#   diag_2_vals = []
#
#   X O _
#   _ O X
#   _ X O
#
#   1, 3 --> 4
#   2, 2 --> 4
#   3, 1 --> 4
#
#   diagonal 1 --> all elements where row = col
#   diagonal 2 --> all elements where row + col is num_rows + 1
#
#   for row in grid:
#     for col in grid[row]:
#       if row == col:
#         diag_1_vals.append(grid[row][col])
#
#     for row in grid:
#       for col in grid[row]:
#         if row + col == 4:
#           diag_2_vals.append(grid[row][col])
#
#     if diag_1_vals  or diag_2_vals == X_win
#       return X_WON
#     if diag_1_vals or diag_2_vals = O_win
#       return O_WON
#
#     return NOT_OVER
#
# initialize_game(grid, whose_turn):
#   whose_turn = True
#   for row in grid:
#     for col in grid[row]:
#       grid[row, col] = '_'
#
# # Remember to add this to play_game()
# print_grid(grid):
#   for row in grid:
#     for col in grid[row]:
#       print grid[row][col]
#     print newline
#
# play_game():
#
#   # DO THIS AT BEGINNING
#   grid = 3 x 3 array
#   whose_turn = some boolean
#   initialize_game(grid, whose_turn)
#   # After calling, we know grid is filled with empties,
#   # and we know that we have set whose_turn so that it is X's move
#
#   print_grid(grid)
#
#   # Keep asking for moves until the game is over
#   game_status = NOT_OVER
#   moves_made = 0
#
#   while game_status == NOT_OVER:
#     move_coor = get_move(whose_turn)
#     # After calling get_move once we have some move
#     make_move(move_coor, whose_turn, grid)
#     # After calling make_move we know some valid move was made
#     print_grid(grid)
#     # Change whose turn it is:
#     whose_turn = !whose_turn
#
#     moves_made = moves_made + 1
#
#     # Only determine game status if at least 6 moves were made
#     if moves_made >= 6:
#       game_status = get_game_status(grid)
#     else:
#       game_status = NOT_OVER
#
#   if game_status == X_WON:
#     print 'X Won'
#   elif game_status == O_WON:
#       print 'O Won'
#   else:
#       print 'Draw'
#
#
# Scratch Work:
#
#
#   [['_', '_', '_']
#    ['X'  'X'  'X']
#    ['X'  'O'  'O']]
#
#   counter <- 0
#
#   for row in grid:                 we are in row 3
#     for col in grid[row]:          we are in col 3 of row 3
#       counter <- counter + 1       counter = 9

# ----------------------- WRITING CODE ------------------------
import numpy as np

DRAW = 0
X_WON = 1
O_WON = 2
NOT_OVER = 3

def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def make_move(move_coordinate, whose_turn, grid):
    # Making sure we have a valid move
	valid = is_move_valid(grid, move_coordinate)

	while valid is False:
		print "Your move is invalid, please enter a proper move!!!"
		move_coordinate = get_move(whose_turn)
		valid = is_move_valid(grid, move_coordinate)

	# Now we know that we have a valid move
	# Making our valid move
	if whose_turn is True:
		grid[move_coordinate[0], move_coordinate[1]] = 'X'
	else:
		grid[move_coordinate[0], move_coordinate[1]] = 'O'

def is_move_valid(grid, coordinate):
	# Check if the coordinate is in bounds
	# Row and columns need to be both in the interval (0, 3]
	# coordinate = (row, col)

	if not (coordinate[0] >= 0 and coordinate[0] < 3 and coordinate[1] >= 0 and coordinate[1] < 3):
		return False

	# We only get here if the move is in bounds so now we need
	# to see if the coordinate in the grid is empty
	if grid[coordinate[0], coordinate[1]] == '_':
		return True
	else:
		return False

def get_move(whose_turn):
	if whose_turn:
		print "Hi player X please type a move in the format row col"
	else:
		print "Hi player O please type a move in the format row col"

	response_good = False

	while not response_good:
  		user_response = raw_input()
  		user_response = user_response.split()

		if len(user_response) != 2:
			response_good = False
			print "Hey user you inputted the wrong amount of arguments!"
		elif not (is_int(user_response[0]) and is_int(user_response[1]) ):
			response_good = False
			print "Hey user you put the right amount of arguments but they are not integers!"
		else:
			response_good = True

	return ( int(user_response[0]), int(user_response[1])  )

def check_if_board_full(grid):
	for row_index in range(len(grid)):
		for col_index in range(len(grid[row_index])):
			if grid[row_index, col_index] == '_':
				return False

	return True

def initialize_game(grid, whose_turn):
	whose_turn = True
	for row_index in range(len(grid)):
		for col_index in range(len(grid[row_index])):
	  		grid[row_index, col_index] = '_'

def print_grid(grid):
	for row_index in range(len(grid)):
		row_str = ""
		for col_index in range(len(grid[row_index])):
			row_str += (str(grid[row_index, col_index]) + " ")
		print row_str

def get_game_status(grid):
	X_win = np.array(['X', 'X', 'X'])
	O_win = np.array(['O', 'O', 'O'])

	# Check rows
	for row_index in range(len(grid)):
		if np.array_equal(grid[row_index], X_win):
			return X_WON
		elif np.array_equal(grid[row_index], O_win):
			return O_WON

	# Check columns
	for col_index in range(len(grid[0])):
		if np.array_equal(grid[:, col_index], X_win):
			return X_WON
		elif np.array_equal(grid[:, col_index], O_win):
			return O_WON

	# Check diagonals
	diag_1_vals = []
	diag_2_vals = []

	for row_index in range(len(grid)):
		for col_index in range(len(grid[row_index])):
			if row_index == col_index:
				diag_1_vals.append(grid[row_index][col_index])

	for row_index in range(len(grid)):
		for col_index in range(len(grid[row_index])):
			if row_index + col_index == (len(grid) + 1):
				diag_2_vals.append(grid[row_index][col_index])

	diag_1_vals = np.array(diag_1_vals)
	diag_2_vals = np.array(diag_2_vals)

	if np.array_equal(diag_1_vals, X_win) or np.array_equal(diag_2_vals, X_win):
		return X_WON
	if np.array_equal(diag_1_vals, O_win) or np.array_equal(diag_2_vals, O_win):
		return O_WON

	if check_if_board_full(grid):
		return DRAW

	return NOT_OVER

def play_game():
	grid = np.chararray((3, 3))
	whose_turn = True
	initialize_game(grid, whose_turn)
	# After calling, we know grid is filled with empties,
	# and we know that we have set whose_turn so that it is X's move
	print_grid(grid)
	# Keep asking for moves until the game is over
	game_status = NOT_OVER
	moves_made = 0

	while game_status == NOT_OVER:
		move_coor = get_move(whose_turn)
		# After calling get_move once we have some move
		make_move(move_coor, whose_turn, grid)
		# After calling make_move we know some valid move was made
		print_grid(grid)
		# Change whose turn it is:
		whose_turn = not whose_turn
		moves_made = moves_made + 1
		# Only determine game status if at least 6 moves were made
		if moves_made >= 5:
			game_status = get_game_status(grid)
		else:
			game_status = NOT_OVER

	if game_status == X_WON:
		print 'Game Over: X Won'
	elif game_status == O_WON:
		print 'Game Over: O Won'
	else:
		print 'Game Over: Draw'

# ----------------------- RUN CODE ------------------------
play_game()
