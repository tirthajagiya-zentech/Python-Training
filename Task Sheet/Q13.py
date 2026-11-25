# Create a Tic Tac Toe game in python.
#
# 1. You should be able to play with two players.
# 2. You should be able to play against computer.
#
# After you complete simple game implement it in a way that computer never loses.

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def show_board():
    print("************************")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print("************************")


def place_sign(pos, sign):
    for i in range(3):
        for j in range(3):
            if board[i][j] == pos:
                board[i][j] = sign
                return True
    return False


def check_row(sign):
    for i in range(3):
        temp = 0
        for j in range(3):
            if board[i][j] == sign:
                temp += 1
        if temp == 3:
            return True
    return False


def check_col(sign):
    for i in range(3):
        temp = 0
        for j in range(3):
            if board[j][i] == sign:
                temp += 1
        if temp == 3:
            return True
    return False


def check_diag(sign):
    temp = 0
    for i in range(3):
        if board[i][i] == sign:
            temp += 1
    return temp == 3


def check_anti_diag(sign):
    temp = 0
    for i in range(3):
        if board[i][2 - i] == sign:
            temp += 1
    return temp == 3


def is_winner(sign):
    return check_row(sign) or check_col(sign) or check_diag(sign) or check_anti_diag(sign)


def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ("O", "X"):
                return False
    return True


def minimax(is_max):
    if is_winner("X"):
        return 1
    if is_winner("O"):
        return -1
    if is_full():
        return 0

    if is_max:
        best = -10
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ("O", "X"):
                    old = board[i][j]
                    board[i][j] = "X"
                    best = max(best, minimax(False))
                    board[i][j] = old
        return best
    else:
        best = 10
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ("O", "X"):
                    old = board[i][j]
                    board[i][j] = "O"
                    best = min(best, minimax(True))
                    board[i][j] = old
        return best


def computer_move():
    best_score = -10
    best_pos = None
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ("O", "X"):
                old = board[i][j]
                board[i][j] = "X"
                score = minimax(False)
                board[i][j] = old
                if score > best_score:
                    best_score = score
                    best_pos = (i, j)
    if best_pos is not None:
        board[best_pos[0]][best_pos[1]] = "X"


print("1. Two Players")
print("2. Vs Computer")
mode = int(input("Choose Mode (1 or 2) : "))

count = 0
while True:
    sign = "O" if count % 2 == 0 else "X"
    print("-------------------")
    if mode == 2 and count % 2 != 0:
        print("Computer Turn (X)")
        print("-------------------")
        computer_move()
    else:
        player_num = "1" if count % 2 == 0 else "2"
        print(f"Player {player_num} Sign {sign}")
        print("-------------------")
        show_board()
        try:
            user_pos = int(input("Enter Position Number (1-9) : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not place_sign(user_pos, sign):
            print("Invalid or already taken position, try again.")
            continue

    show_board()

    if is_winner(sign):
        if mode == 2 and count % 2 != 0:
            print("Winner : Computer")
        else:
            player_num = "1" if count % 2 == 0 else "2"
            print(f"Winner : Player {player_num}")
        break

    if is_full():
        print("Match Draw!")
        break

    count += 1
