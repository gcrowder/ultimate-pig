from pig import Player


def test_create_player_rolls_holds():
    bob = Player()
    assert bob.strategy == ['roll', 'hold']
