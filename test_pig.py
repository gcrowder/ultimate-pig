from pig import *
from unittest import mock


def test_create_player_rolls_holds():
    bob = Player()
    assert bob.strategy == ['roll', 'hold']


def test_create_player_total_zero():
    bill = Player()
    assert bill.total == 0


def test_add_to_player_total():
    jeff = Player()
    jeff.add_to_total(1)
    assert jeff.total == 1

anne = Player()


def test_player_choice_roll():
    assert anne.choice(1) == 'roll'


def test_player_choice_hold():
    assert anne.choice(1) == 'hold'


@mock.patch('random.randint')
def test_roll(mock_random):
    mock_random.return_value = 6
    assert roll_die() == 6


@mock.patch('random.randint')
def test_turn(mock_random):
    mock_random.return_value = 6
    joe = Player()
    assert turn(joe, 1) == 6


# @mock.patch('random.randint')
# def test_game_loop(mock_random):
#     mock_random.return_value = 1
