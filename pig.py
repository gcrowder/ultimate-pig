import random


class Player:
    def __init__(self):
        self.total = 0
        self.turn_amount = 0

    def choice(self, turn):
        if self.turn == turn:
            return self.strategy[1]
        else:
            self.turn = turn
            return self.strategy[0]

    # def add_to_total(self, number):
    #     self.total += number

    def is_roll_again(self):
        return False


def roll_die():
    return random.randint(1, 6)


def play(player):
    total = player.total
    roll = roll_die()
    if roll == 1:
        return total
    else:
        total += roll
        return total


def game_loop(player):
    result = 0
    for turn in range(7):
        result = play(player)
        player.total = result
        while player.is_roll_again():
            result = play(player)
            player.total = result
    return player.total


def main():
    player_class_trials = []
    for _ in range(1):
        bob = Player()
        player_class_trials.append(game_loop(bob))
    print("List: ", player_class_trials)

if __name__ == '__main__':
    main()
