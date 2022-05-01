# Tic-Tac-Toe game for CSE210
###

from shutil import move


def main():
    banner = '#'
    welcome_msg = 'Let´s play Tic-Tac-Toe'
    movements_list = []

    print(banner*40 + '\n' + ' '*8 + welcome_msg + '\n' + banner*40)

    print_game(movements_list)
    while


def check_movement(already_occupied, new_movement):

    move = False

    if new_movement in already_occupied:
        print('Space already Occupied')
    else:
        already_occupied.append(new_movement)
        move = True
    return move


def save_valid_movement(movements_list, player):

    movements_list.append(player)
    return movements_list


def check_win(movements_list, player):

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
        result = 'winner'
    return result


def print_game(movements_list):
    if len(movements_list) == 0:
        for i in range(9):
            if i in (2, 5, 8):
                print("|"+str(i+1)+"|\n", end="")
            else:
                print("|"+str(i+1)+"|", end="")
    else:
        for i in range(8):
            if movements_list[i] != '':
                if i in (2, 5, 8):
                    print("|"+movements_list[i]+"|\n", end="")
                else:
                    print("|"+movements_list[i]+"|", end="")
            else:
                if i in (2, 5, 8):
                    print("|"+str(i+1)+"|\n", end="")
                else:
                    print("|"+str(i+1)+"|", end="")


if __name__ == "__main__":
    main()
