import random
board = [[' ' for x in range(3)] for y in range(3)]
game_over = False

def print_board():
    for row in board:
        print('|'.join(row))

def check_for_win():
    global game_over
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            print("Player " + board[i][0] + " wins!")
            game_over = True
            return
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            print("Player " + board[0][i] + " wins!")
            game_over = True
            return
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        print("Player " + board[0][0] + " wins!")
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        print("Player " + board[0][2] + " wins!")
        game_over = True
        return

def check_for_draw():
    global game_over
    for row in board:
        for cell in row:
            if cell == ' ':
                return
    print("It's a draw!")
    game_over = True

def make_move(player, row, col):
    if board[row][col] != ' ':
        print("Invalid move! Try again.")
        return
    board[row][col] = player

while not game_over:
    print_board()
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter column (0, 1, 2): "))
    make_move('X', row, col)
    check_for_win()
    check_for_draw()
    if game_over:
        break
    # computer's turn
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            make_move('O', row, col)
            check_for_win()
            check_for_draw()
            break
