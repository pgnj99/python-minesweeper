import board as b

def play(choice):
    # Guesses set will contain all of player's guesses
    guesses = set()
    
    # Choices 1 to 4 indicate different difficulty levels
    # Boards will be made based on difficulty specifications
    if choice == 1:
        board = b.make_board(5, 5, 7)
    if choice == 2:
        board = b.make_board(8, 8, 10)
    if choice == 3:
        board = b.make_board(16, 16, 40)
    if choice == 4:
        board = b.make_board(25, 25, 70)
        
    if choice == 'Papegay':
        board = b.make_board_classic()
    
    # Choice 5 is custom board
    # Player can decide their own board size and mine total
    elif choice == 5:
        # Loops are used for each parameter for input validation
        # Game will otherwise crash if non-numeric value is entered
        while True:
            height = input('Enter number of rows (1 - 25):')
            if height.isnumeric():
                # Maximum row count is 25
                if int(height) < 1 or int(height) > 25:
                    print('Invalid row count.')
                else:
                    break
            else:
                print('Invalid row count.')
        while True:
            width = input('Enter number of columns (1 - 25):')
            if width.isnumeric():
                if int(width) < 1 or int(width) > 25:
                # Maximum column count is 25
                    print('Invalid column count.')
                else:
                    break
            else:
                print('Invalid column count.')
        
        # Board can only contain as many mines as there are available spaces
        area = int(height) * int(width)
        while True:
            # 0 mine board is allowed in order for 1x1 board to exist
            mines = input('Enter number of mines (0 - ' + str(area - 1) + '):')
            if mines.isnumeric:
                if int(mines) < 0 or int(mines) > area - 1:
                    print('Invalid mine count.')
                else:
                    break
            else:
                print('Invalid mine count.')
        
        board = b.make_board(int(height), int(width), int(mines))
    
    # This loop will run for as long as the game is active
    while True:
        # Full board will be displayed after every guess
        b.display_board(board, guesses)
        
        # Game will immediately end upon win or loss
        if b.check_board(board) == 'L':
            print('Game Over!')
            break
        elif b.check_board(board) == 'W':
            print('You Win!')
            if choice != 'Papegay':
                print('Enter Papegay to play a special board!')
            break
        
        # Columns will be denoted with letters rather than numbers
        endcol = chr(len(board[0]) + 64)
        
        # Columns require unique input validation loop to check letter
        while True:
            col = input('What column would you like to check? (A - ' + endcol + ')').upper()
            # Input must be not only alphabetical but also only one letter long
            if col.isalpha() and len(col) == 1:
                if ord(col) - 64 < 1 or ord(col) - 64 > len(board[0]):
                    print('Invalid column name.')
                else:
                    break
            else:
                print('Invalid column name.')

        while True:
            row = input('What row would you like to check? (1 - ' + str(len(board)) + ')')
            if row.isnumeric():
                if int(row) < 1 or int(row) > len(board):
                    print('Invalid row name.')
                else:
                    break
            else:
                print('Invalid row name.')
        
        # Guesses will be structured as column first and then row (A1, H5, etc.)
        guesses.add(col + row)