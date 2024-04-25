print("Welcome, this is tic-tac-toe")
print("Players select their icons and play the game")
player1 = input("Enter name of player N1: ")
player2 = input("Enter name of player N2: ")
print(f"Game has started, player N1 is {player1} and player N2 is {player2}")

board = [str(i+1) for i in range(9)]
def board_func():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print(" ")
    print(row1)
    print(row2)
    print(row3)
    print(" ")


def main_func(player, icon):
    while True:
        try:
            a = int(input(f"{player}, Enter an integer 1-9: ")) - 1
        except ValueError:
            print("Error, enter again.")
            board_func()
            continue
        if 0 <= a <= 8 and board[a] in "123456789":
            board[a] = icon
            board_func()
            break
        else:
            print("Error, Enter again.")
            board_func()


def victory(icon):
    correct_arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 8]]
    for arr in correct_arr:
        if all(board[i] == icon for i in arr):
            return True
        return False


def tic_tac_toe():
    counter = 0
    while True:

        main_func(player1, "X")
        counter += 1

        if victory("X"):
            print(f"{player1} wins!")
            break

        if counter == 9:
            print("Game ended with a draw!")
            break

        main_func(player2, "O")
        counter += 1

        if victory("O"):
            print(f"{player2} wins!")
            break


board_func()
tic_tac_toe()
