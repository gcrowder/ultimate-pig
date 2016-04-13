import random


class Player:
    def __init__(self):
        self.strategy = ['roll', 'hold']


def roll():
    return random.randint(1, 6)
