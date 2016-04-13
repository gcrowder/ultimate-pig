from pig import *
from unittest import mock


def test_create_player_rolls_holds():
    bob = Player()
    assert bob.strategy == ['roll', 'hold']


def test_create_player_total_zero():
    bill = Player()
    assert bill.total == 0


@mock.patch('random.randint')
def test_roll(mock_random):
    mock_random.return_value = 6
    assert roll_die() == 6


@mock.patch('random.randint')
def test_turn(mock_random):
    mock_random.return_value = 6
    joe = Player()
    assert turn(joe) == 6
