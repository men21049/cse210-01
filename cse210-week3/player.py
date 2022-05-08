class player:

    def __init__(self):
        self.name = ""
        self.score = 300

    def increase_score(self, inc):
        self.score += inc

    def decrease_score(self, dec):
        self.score -= dec
