from constants import RPS_MOVES, WIN_MOVES
from typing import NamedTuple, List


class NoSuchStrategyError(ValueError):
    """ Raise this error if there is a wrong move in rps_game_winner. """
    pass


class WrongNumberOfPlayersError(ValueError):
    """ Raise this error if there is a wrong count of players in rps_game_winner. """
    pass


class Player(NamedTuple):
    name: str
    move: str


def rps_game_winner(players: List[List[str]]) -> str:
    """
    Return the winner player and his move in rps game.
    If the moves are the same, the first player wins.
    If more than 2 players, raise WrongNumberOfPlayersError.
    If player's move hasn't one is ['R', 'P', 'S'], raise NoSuchStrategyError.
    """

    check_count_of_players(players)
    player_one, player_two = (Player(name=name, move=move) for name, move in players)
    is_correct_moves(player_one, player_two)
    player_winner = choose_winner(player_one, player_two)

    return f'{player_winner.name} {player_winner.move}'


def check_count_of_players(players: List[List[str]]):
    """ Checking count of players. If player's count doesn't equal two then raise WrongNumberOfPlayersError. """
    if len(players) != 2:
        raise WrongNumberOfPlayersError(
            f"Incorrect players in game: got {len(players)}, expected 2")


def is_correct_moves(player_one: Player, player_two: Player):
    """ Checking that the moves are correct else raise NoSuchStrategyError. """
    for player in (player_one, player_two):
        if player.move not in RPS_MOVES:
            raise NoSuchStrategyError(
                f"Incorrect player's move: expected {RPS_MOVES=}, but got {player.move=}")


def choose_winner(player_one: Player, player_two: Player) -> Player:
    """
    Return a winner in rps game. If the moves are the same, will be chosen the first player.
    Get the ASCII code of moves ('R' : 82, 'S' : 83, 'P' : 80). The first player wins if the difference
    between the ASCII codes of his move and the second players are equal (-1, -2, 0, 3).
    """

    player_one_move = ord(player_one.move)
    player_two_move = ord(player_two.move)
    moves_result = player_one_move - player_two_move

    return player_one if moves_result in WIN_MOVES else player_two

