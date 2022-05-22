#!/usr/bin/env python
# #########################################
# Class player defines a player in the game,
# it has 4 methods:
# __init__ : initializes the class with an empty
# name and a min score of 300
# increase_score : which increases the score
# decrease_score : which decreases the score
# inc_or_dec : determines whether the score must
# increment or decrease base on a comparisson of the players answers
# keep_playing: determines whether a player wants to exit out of
# the fame or keep playing after every play or if the score is less than 0
__author__ = "Juan Carlos Mena Osorio"
__credits__ = ["Professor Vaughn Poulson, BYU-I"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Juan Carlos Mena Osorio"
__status__ = "Development"
#########################################


class player:

    def __init__(self):
        self.name = ""
        self.score = 300

    def increase_score(self, inc):
        self.score += inc

    def decrease_score(self, dec):
        self.score -= dec

    def inc_or_dec(self, answer, compare):
        if answer == compare:
            self.increase_score(100)
        else:
            self.decrease_score(75)

    def keep_playing(self):
        keep_playing = True

        if self.score <= 0:
            print("GAME OVER")
            keep_playing = False

        kp = input("Play again? [y/n] ")

        if kp == "n":
            keep_playing = False
        return keep_playing
