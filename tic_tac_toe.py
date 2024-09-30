
def create_board():
    return ['-' for _ in range(9)]


def show_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()


def check_winner(board, player):
   
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)


def is_board_filled(board):
    for row in board:
        if row == '-':
            return False
    return True


def start_game():
    board = create_board()
    current_player = 'X'
    
    while True:
        show_board(board)
        print(f"Player {current_player}'s turn.")
        
       
        move = int(input("Choose your position (1-9): ")) - 1
        
        if board[move] == '-':
            board[move] = current_player
        else:
            print("Spot taken. Try again.")
            continue
        
      
        if check_winner(board, current_player):
            show_board(board)
            print(f"Player {current_player} wins!")
            break
        
     
        if  is_board_filled(board):
            show_board(board)
            print("It's a draw!")
            break
        
        
        current_player = 'O' if current_player == 'X' else 'X'


start_game()
