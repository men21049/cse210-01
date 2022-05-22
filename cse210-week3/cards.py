#!/usr/bin/env python
# #########################################
# Class cards, it has 3 methods:
# __init__ : constructore class to instantiate cards
# get_random_card: it return a random numbre from the array[1 .. to .. 13]
# compare_cards : it compares the values of 2 already draw cards and returns
#                 "l" for lower and "h" for higher
__author__ = "Juan Carlos Mena Osorio"
__credits__ = ["Professor Vaughn Poulson, BYU-I"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Juan Carlos Mena Osorio"
__status__ = "Development"
#########################################
import random


class cards:

    def __init__(self):
        self.card_list = [i + 1 for i in range(13)]

    def get_random_card(self):
        random_number = random.choice(self.card_list)
        return random_number

    def compare_cards(self, card1, card2):
        result = ""
        if card1 > card2:
            result = "l"
        else:
            result = "h"
        return result
