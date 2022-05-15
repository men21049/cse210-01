from cards import cards
from player import player


def main():

    keep_playing = True
    playr = player()
    name_player = input("What is your name? :")
    playr.name = name_player

    while keep_playing:

        card = cards()
        card1 = card.get_random_card()
        print(f'OK {playr.name}, let´s play')
        print(f'The card is: {card1} ')
        answer = input("Higher or lower? [h/l] ")
        card2 = card.get_random_card()
        print(f'Next card was: {card2}')
        compare = compare_cards(card1, card2)

        if answer == compare:
            playr.increase_score(100)
        else:
            playr.decrease_score(75)

        print(f'Your score is: {playr.score}')

        if playr.score <= 0:
            print("GAME OVER")
            keep_playing = False

        kp = input("Play again? [y/n] ")

        if kp == "n":
            keep_playing = False


def compare_cards(card1, card2):
    result = ""
    if card1 > card2:
        result = "l"
    else:
        result = "h"
    return result


if __name__ == "__main__":
    main()
