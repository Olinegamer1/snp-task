from tasks.task_06 import rps_game_winner, NoSuchStrategyError, WrongNumberOfPlayersError


def test_rps_game_winner():
    # Test 1: Test a simple game where the first player wins
    assert rps_game_winner([['Player 1', 'R'], ['Player 2', 'S']]) == 'Player 1 R'

    # Test 2: Test a simple game where the second player wins
    assert rps_game_winner([['Player 1', 'P'], ['Player 2', 'S']]) == 'Player 2 S'

    # Test 3: Test a game where both players make the same move
    assert rps_game_winner([['Player 1', 'S'], ['Player 2', 'S']]) == 'Player 1 S'

    # Test 4: Test a game where the first player's move is invalid
    try:
        rps_game_winner([['Player 1', 'A'], ['Player 2', 'S']])
    except NoSuchStrategyError:
        pass
    else:
        raise AssertionError("Expected a NoSuchStrategyError to be raised but none was raised")

    # Test 5: Test a game where there are more than two players
    try:
        rps_game_winner([['Player 1', 'R'], ['Player 2', 'P'], ['Player 3', 'S']])
    except WrongNumberOfPlayersError:
        pass
    else:
        raise AssertionError("Expected a WrongNumberOfPlayersError to be raised but none was raised")


if __name__ == '__main__':
    test_rps_game_winner()

