import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)


def player_move():
    move = int(input("Choose position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"

def ai_move():
    empty = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(empty)
    board[move] = "O"

def main():
    print("Tic-Tac-Toe vs AI")
    print_board()

    for _ in range(9):
        player_move()
        print_board()

        if check_winner("X"):
            print("You win!")
            return

        ai_move()
        print_board()

        
        if check_winner("O"):
            print("AI wins!")
            return
        
    print("It's a draw!")
    

main()

