import unittest
from task_06 import rps_game_winner, NoSuchStrategyError, WrongNumberOfPlayersError


class TestRpsGameWinner(unittest.TestCase):

    def test_simple_game_player1_wins(self):
        self.assertEqual(rps_game_winner([['Player 1', 'R'], ['Player 2', 'S']]), 'Player 1 R')

    def test_simple_game_player2_wins(self):
        self.assertEqual(rps_game_winner([['Player 1', 'P'], ['Player 2', 'S']]), 'Player 2 S')

    def test_game_with_same_moves(self):
        self.assertEqual(rps_game_winner([['Player 1', 'S'], ['Player 2', 'S']]), 'Player 1 S')

    def test_invalid_move_player1(self):
        with self.assertRaises(NoSuchStrategyError):
            rps_game_winner([['Player 1', 'A'], ['Player 2', 'S']])

    def test_wrong_number_of_players(self):
        with self.assertRaises(WrongNumberOfPlayersError):
            rps_game_winner([['Player 1', 'R'], ['Player 2', 'P'], ['Player 3', 'S']])
