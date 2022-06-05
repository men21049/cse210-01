#!/usr/bin/env python
# #########################################

__author__ = "Juan Carlos Mena Osorio"
__credits__ = ["Professor Vaughn Poulson, BYU-I"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Juan Carlos Mena Osorio"
__status__ = "Development"
#########################################
import random


class Cards:
    """Cards class is designed to play hilo, the constructor: __init__ creates a list of cards to play.
       The method get_random_card, helps returning a card selected randomnly.
       Compare_cards method, returns l or h for whether a card is lower or higher than another.
    """

    def __init__(self):
        """ This method creates a list of cards(numbers) between 1 and 12.
        """
        self.card_list = [i + 1 for i in range(13)]

    def get_random_card(self):
        """ This method select a card to play randomly

        Returns:
            number: returns the variable name random_number, which is the selected random number from the card_list 
            list. 
        """
        random_number = random.choice(self.card_list)
        return random_number

    def compare_cards(self, card1, card2):
        """ This method compares 2 cards and returns l or h , lower or higher, this means that the 1st card
        can be lower(l) or higher(h) than the second card.

        Args:
            card1 (number): 1st card to compare
            card2 (number): 2nd card to compare

        Returns:
            string: it could return 2 possible values, l for lower or h for higher.
        """
        result = ""
        if card1 > card2:
            result = "l"
        else:
            result = "h"
        return result
