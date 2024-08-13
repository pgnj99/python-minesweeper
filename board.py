import random

# This board is based on this image: https://www.researchgate.net/figure/Windows-famous-Minesweeper-board_fig1_270040838
# I used this original function as a placeholder before working on the main make_board function
# Just for fun, I've decided to keep it as an easter egg
def make_board_classic():
    board = []
    board.append(['#', '*', '#', '#', '#', '*', '#', '#'])
    board.append(['#', '#', '#', '#', '#', '#', '#', '#'])
    board.append(['#', '*', '#', '#', '#', '#', '#', '#'])
    board.append(['#', '#', '#', '#', '#', '#', '#', '#'])
    board.append(['*', '#', '#', '#', '#', '#', '#', '#'])
    board.append(['#', '#', '#', '#', '*', '#', '*', '#'])
    board.append(['#', '*', '*', '*', '#', '#', '#', '#'])
    board.append(['#', '#', '#', '#', '#', '*', '#', '#'])
    return board

# This function creates the board to be used
def make_board(height, width, mines):
    board = []
    
    # A random list of mine locations is generated
    minelist = random.sample(range(1, height*width), mines)
    
    # spot will be used to keep track of location while adding mines to board
    spot = 1
    for i in range(height):
        row = []
        for j in range(width):
            if spot in minelist:
                # Mines will be represented by asterisks
                row.append('*')
            else:
                # Safe spaces will be represented by pound signs
                row.append('#')
            spot += 1
        # Rows will be contained as lists within a larger list
        board.append(row)
    
    return board

# This function marks the spot guessed
def mark_board(board, guesses):
    # Each guess in set will be checked
    
    for guess in guesses:
        x = int(guess[1:]) - 1
        y = ord(guess[0]) - 65
        mines = 0
        
        # The player guesses a safe spot
        if board[x][y] == '#':
            # The number put in its place will represent the number of adjacent mines
            # Multiple if statements are required to prevent checking out of bounds on edges
            
            if x > 0:
                if board[x-1][y] == '*':
                    mines += 1
                if y > 0:
                    if board[x-1][y-1] == '*':
                        mines += 1
                if y < len(board) - 1:
                    if board[x-1][y+1] == '*':
                        mines += 1
                        
            if x < len(board[0]) - 1:
                if board[x+1][y] == '*':
                    mines += 1
                if y > 0:
                    if board[x+1][y-1] == '*':
                        mines += 1
                if y < len(board) - 1:
                    if board[x+1][y+1] == '*':
                        mines += 1
                        
            if y > 0:
                if board[x][y-1] == '*':
                    mines += 1
            if y < len(board) - 1:
                if board[x][y+1] == '*':
                    mines += 1
            
            # Set space to number of adjacent mines
            board[x][y] = str(mines)
            
            # When hitting a 0, all adjacent squares will be revealed as well
            if mines == 0:
                # A list of all adjacent squares will run through this function again
                # This may repeat until all adjacent 0's in area are revealed
                zero_square = []
                if x > 0:
                    zero_square.append(chr(y + 65) + str(x + 0))
                    if y > 0:
                        zero_square.append(chr(y + 64) + str(x + 0))
                    if y < len(board) - 1:
                        zero_square.append(chr(y + 66) + str(x + 0))
                        
                if x < len(board[0]) - 1:
                    zero_square.append(chr(y + 65) + str(x + 2))
                    if y > 0:
                        zero_square.append(chr(y + 64) + str(x + 2))
                    if y < len(board) - 1:
                        zero_square.append(chr(y + 66) + str(x + 2))
                        
                if y > 0:
                    zero_square.append(chr(y + 64) + str(x + 1))
                if y < len(board) - 1:
                    zero_square.append(chr(y + 66) + str(x + 1))
            
                mark_board(board, zero_square)
        
        # When hitting a mine, an X will be marked in its place
        elif board[x][y] == '*':
            board[x][y] = 'X'
            
    return board

# This function displays the board after every guess
def display_board(board, guesses):
    board = mark_board(board, guesses)
    
    row = 1
    col = 1
    
    # Header will display letters representing each column
    print('   ', end = ' ')
    for num in range(len(board[0])):
        print(chr(num + 65), end = ' ')
    print()
    
    for line in board:
        # Each row below header will start with number
        # To keep columns in-line, numbers less than 10 will be spaced to the right
        if row < 10:
            print(end = ' ')
        print(str(row) + '|', end = ' ')
        
        for space in line:
            # Alphanumeric spaces represent those guessed by the player
            if space.isalnum():
                print(space, end = ' ')
            # Unguessed spaces are marked as filled squares (■)
            else:
                print('■', end = ' ')
        print()
        row += 1
    
    return board

# This function checks the board for win or loss
def check_board(board):
    safe = 0
    for line in board:
        for space in line:
            # An X on the board represents a hit mine; the player loses
            if space == 'X':
                return 'L'
            # Number of safe spaces is counted
            if space == '#':
                safe += 1
    
    # The player wins when no safe spaces are left
    if safe > 0:
        return 'P'
    else:
        return 'W'