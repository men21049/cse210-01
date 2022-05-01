# Tic-Tac-Toe game for CSE210
###

from operator import truediv
from shutil import move


def main():
    banner = '#'
    welcome_msg = 'Let´s play Tic-Tac-Toe'
    movements_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    not_yet_winner = True
    already_occupied = []
    print(banner*40 + '\n' + ' '*8 + welcome_msg + '\n' + banner*40)
    player_x = input("Set 1st Player, name : ")
    player_0 = input("Set 2nd Player, name : ")
    answer = "Yes"
    print_game(movements_list)

    while not_yet_winner:

        keep_playing = play(player_x, already_occupied, movements_list, "x")
        if keep_playing == "No":
            answer = input("Do you want to play again (yes/no)? ")
        keep_playing = play(player_0, already_occupied, movements_list, "0")
        if keep_playing == "No":
            answer = input("Do you want to play again (yes/no)? ")
        if len(already_occupied) == 9:
            print("It is a tie")
            answer = input("Do you want to play again (yes/no)? ")
            if answer == "yes":
                clear_lists(already_occupied, movements_list)
        if answer == "no":
            not_yet_winner = False


def clear_lists(already_occupied, movements_list):
    already_occupied.clear()
    for i in range(len(movements_list)):
        movements_list[i] = str(i+1)


def play(player, already_occupied, movements_list, flag):
    is_valid = True
    keep_playing = "Yes"
    if len(already_occupied) == 9:
        is_valid = False
    while is_valid:
        make_a_move = int(
            input("Make a move " + player + ", select a number from the display: "))

        check_mov = check_movement(already_occupied, make_a_move)

        if check_mov:
            save_valid_movement(movements_list, make_a_move-1, flag)
            print_game(movements_list)
            is_win = check_win(movements_list, flag)

            if is_win == "winner":
                print(player + ", you WIN!!!!")
                keep_playing = "No"
                break
            is_valid = False

        else:
            print("Please type another place")
    return keep_playing


def check_movement(already_occupied, new_movement):

    move = False

    if new_movement in already_occupied:
        print('Space already Occupied')
    else:
        already_occupied.append(new_movement)
        move = True
    return move


def save_valid_movement(movements_list, key, player):

    if key >= 0 and key <= 8:
        movements_list[key] = player
    return movements_list


def check_win(movements_list, player):

    result = "Not winner"
    # first win:
    # 1,2,3 belong to the same player:
    if((movements_list[0] == player and movements_list[1] == player and movements_list[2] == player)
        # Second win:
        # 4,5,6 belong to the same player:
        or (movements_list[3] == player and movements_list[4] == player and movements_list[5] == player)
        # Third win:
        # 7,8,9 belong to the same player:
        or (movements_list[6] == player and movements_list[7] == player and movements_list[8] == player)
        # Fourth win:
        # 1,4,7 belong to the same player:
        or (movements_list[0] == player and movements_list[3] == player and movements_list[6] == player)
        # Fifth win:
        # 2,5,8 belong to the same player:
        or (movements_list[1] == player and movements_list[4] == player and movements_list[7] == player)
        # sixth win:
        # 3,6,9 belong to the same player:
        or (movements_list[2] == player and movements_list[5] == player and movements_list[8] == player)
        # seventh win:
        # 1,5,9 belong to the same player
        or (movements_list[0] == player and movements_list[4] == player and movements_list[8] == player)
        # eight win:
        # 3,5,7 belong to the same player:
            or (movements_list[2] == player and movements_list[4] == player and movements_list[6] == player)):
        result = "winner"
    return result


def print_game(movements_list):
    for i in range(len(movements_list)):
        if i in (2, 5, 8):
            print("|"+movements_list[i]+"|\n", end="")
        else:
            print("|"+movements_list[i]+"|", end="")


if __name__ == "__main__":
    main()
