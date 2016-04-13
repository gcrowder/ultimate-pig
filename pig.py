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


def play(player, turn):
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


def game_loop(player):
    result = 0
    for turn in range(7):
        result = play(player, turn)
        while player.total != result:
            player.add_to_total(result)
            result = play(player, turn)
            player.next_turn()
    return player.total
