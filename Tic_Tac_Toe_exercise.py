previous_placements = []

first_row = ["_", "_", "_"]
second_row = ["_", "_", "_"]
third_row = ["_", "_", "_"]
board = [first_row, second_row, third_row]

# print(board)

first_row_reference = ["1", "2", "3"]
second_row_reference = ["4", "5", "6"]
third_row_reference = ["7", "8", "9"]


def get_player_input():
    choice = ""
    # choice needs to be a digit, and between 1 and 9
    allowed_range = range(1, 10)

    while choice.isdigit() is False or choice in previous_placements or int(choice) not in allowed_range:
        choice = input("please input a number from 1 to 9: ")
        if choice == "reference":
            print_reference()
            continue
        elif choice == "exit":
            print("thanks for playing! bye!")
            exit()
            continue
        elif choice in previous_placements:
            print("oops, choice already claimed! pick another spot!")
        elif choice.isdigit() is False or int(choice) not in allowed_range:
            print("only numbers from 1 to 9 please!")

    previous_placements.append(choice)
    return int(choice)


def print_board():
    print(first_row)
    print(second_row)
    print(third_row)


def print_reference():
    print(first_row_reference)
    print(second_row_reference)
    print(third_row_reference)


def update_board(symbol):
    choice = get_player_input()
    if choice in range(1, 4):
        #change symbol on first row
        choice -= 1
        first_row[choice] = symbol
        return first_row
    elif choice in range (4, 7):
        #change symbol on second row
        choice -= 4
        second_row[choice] = symbol
        return second_row
    else:
        #change symbol on third row
        choice -= 7
        third_row[choice] = symbol
        return third_row


def assign_symbol(turn_number):
    symbol = "X"
    if turn_number % 2 == 0:
        symbol = "0"
    return symbol


def is_game_won():
    winning_cross = ["X", "X", "X"]
    winning_circles = ["0", "0", "0"]
    rows = first_row + second_row + third_row

    # check vertical win
    for n in range(0,3):
        if rows[n] == rows[n+3] == rows[n+6] and (rows[n] == "0" or rows[n] == "X"):
            return True
    # check diagonal win
    if (rows[2] == rows[4] == rows[6] or rows[0] == rows[4] == rows[8]) and (rows[4] == "0" or rows[4] == "X"):
        return True
    # check horizontal win
    for row_list in board:
        if row_list == winning_cross or row_list == winning_circles:
            return True
    return False


def announce_win(symbol):
    print(f'Congrats! {symbol} won!')
    exit_the_game()


def reset_the_table():
    global previous_placements, first_row, second_row, third_row
    previous_placements = []
    first_row = ["_", "_", "_"]
    second_row = ["_", "_", "_"]
    third_row = ["_", "_", "_"]


def exit_the_game():
    reset_the_table()
    print("Thanks for playing! Do you wanna play again?")
    play_again = ""
    while play_again != "N" and play_again != "Y":
        play_again = input("Input Y or N").upper().strip()
        if play_again != "N" and play_again != "Y":
            print("oops! I don't understand.")
    if play_again == "Y":
        play_the_game()
    elif play_again == "N":
        print("Goodbye!")
        exit()

def play_the_game():
    # choice = "0"
    print("\n \n \n1welcome to the game of Tic-Tac-Toe!")
    print("if you need help, type 'reference'")
    print("and if you want to exit the game: type 'exit'")
    print("otherwise, choose your move and have fun! :)")
    print_board()
    i = 1

    while i < 10:
        symbol = assign_symbol(i)
        update_board(symbol)
        print_board()
        if (is_game_won()):
            announce_win(symbol)
        i += 1
    else:
        print("oops! No winners!")
        exit_the_game()


play_the_game()
