# Tic-Tac-Toe Program
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + "   |   ".join(str(cell) for cell in row) + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid = False
    while not valid:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid input! Choose a number between 1 and 9.")
                continue

            move -= 1
            row = move // 3
            col = move % 3
            # Check if the square is occupied
            sign = board[row][col] 
            if sign in ['O', 'X']:
                print("Square is already occupied, choose another input!")
                continue

            board[row][col] = 'O' 
            valid = True
        except:
            print("Invalid input")
        

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == "X":
        winner = 'Computer' # Computer's Side
    elif sign == "O":
        winner = 'You' # Human's side
    else:
        winner = None
    cross1 = cross2 = True #Diagonals
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: #Checking row
            return winner
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: #Checking column
            return winner
        if board[i][i] != sign: #Checks diagonal
            cross1 = False
        if board[2 - i][2 - i] != sign: # check 2nd diagonal
            cross2 = False
    if cross1 or cross2:
        return winner
    return None

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        random = randrange(len(free_fields))
        row, col = free_fields[random]
        board[row][col] = 'X'

#Initialize the Game
board = [[row * 3 + column + 1 for column in range(3)] for row in range(3)]
board[1][1] = 'X' # set first 'X' in the middle
human_turn = True
print("Tic Tac Toe")
# Start Game
while True:
    display_board(board)
    if human_turn:
        enter_move(board)
        winner = victory_for(board, "O")
    else:
        draw_move(board)
        winner = victory_for(board, "X")

    if winner:
        display_board(board)
        print(winner, "win!")
        break
    if not make_list_of_free_fields(board):
        break
    human_turn = not human_turn # Flip turn

