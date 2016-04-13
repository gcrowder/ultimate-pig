import random


class Player:
    def __init__(self):
        self.strategy = ['roll', 'hold']
        self.total = 0

    def choice(self):
        return self.strategy[0]


def roll_die():
    return random.randint(1, 6)


def turn(player):
    total = player.total
    choice = player.choice()
    if choice == 'roll':
        roll = roll_die()
        if roll == 1:
            return total
        else:
            total += roll
            return total
    else:
        return total
