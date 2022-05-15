#########################################
# The file instantiate the classes player and cards
# to play hilo game, it has a main method to instantiate the instance of the class
# and within it a while loop to keep playing while the player still wants to play.
#########################################
from cards import cards
from player import player


def main():

    keep_playing = True
    playr = player()
    playr.name = input("What is your name? :")

    while keep_playing:

        card = cards()
        card1 = card.get_random_card()

        print(f'OK {playr.name}, let´s play')
        print(f'The card is: {card1} ')

        answer = input("Higher or lower? [h/l] ")
        card2 = card.get_random_card()

        print(f'Next card was: {card2}')
        compare = card.compare_cards(card1, card2)

        playr.inc_or_dec(answer, compare)

        print(f'Your score is: {playr.score}')

        keep_playing = playr.keep_playing()


if __name__ == "__main__":
    main()
