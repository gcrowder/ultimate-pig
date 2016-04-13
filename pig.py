import random


class Player:
    def __init__(self):
        self.strategy = ['roll', 'hold']
        self.total = 0
        self.turn = 0

    def choice(self, turn):
        if self.turn == turn:
            return self.strategy[1]
        else:
            self.turn = turn
            return self.strategy[0]

    def add_to_total(self, number):
        self.total += number

    def next_turn(self):
        self.turn += 1


def roll_die():
    return random.randint(1, 6)


def turn(player, turn):
    total = player.total
    choice = player.choice(turn)
    if choice == 'roll':
        roll = roll_die()
        if roll == 1:
            return total
        else:
            total += roll
            return total
    else:
        return total
