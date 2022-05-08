import random


class cards:

    def __init__(self):
        self.card_list = [i + 1 for i in range(13)]

    def get_random_card(self):
        random_number = random.choice(self.card_list)
        return random_number
