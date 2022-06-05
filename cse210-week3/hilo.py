#########################################
#!/usr/bin/env python
# The file instantiate the classes player and cards
# to play hilo game, it has a main method to instantiate the instance of the class
# and within it a while loop to keep playing while the player still wants to play.
__author__ = "Juan Carlos Mena Osorio"
__credits__ = ["Professor Vaughn Poulson, BYU-I"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Juan Carlos Mena Osorio"
__status__ = "Development"
#########################################
from cards import Cards
from player import Player


def main():
    """Main method to start game
    """

    keep_playing = True
    playr = Player()
    playr.name = input("What is your name? :")

    while keep_playing:

        card = Cards()
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
    """Call main method to start game
    """
    main()
