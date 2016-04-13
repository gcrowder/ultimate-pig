from pig import *
from unittest import mock


def test_create_player_rolls_holds():
    bob = Player()
    assert bob.strategy == ['roll', 'hold']


@mock.patch('random.randint')
def test_roll(mock_random):
    mock_random.return_value = 6
    assert roll() == 6
