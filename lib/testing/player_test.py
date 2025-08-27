# test_player.py
import pytest
from ..classes.many_to_many import Game, Player, Result


@pytest.fixture(autouse=True)
def reset_class_lists():
    # Reset class-level lists before each test
    Game.all_games = []
    Player.all_players = []
    Result.all = []

def test_player_initialization_and_username():
    player = Player("Alice")
    assert player.username == "Alice"
    assert isinstance(player.username, str)

def test_username_setter_validation():
    player = Player("Bob")
    player.username = "Charlie"
    assert player.username == "Charlie"

    with pytest.raises(ValueError):
        player.username = "A"  # too short
    with pytest.raises(ValueError):
        player.username = 123  # invalid type

def test_player_results_and_games():
    game1 = Game("Skribbl.io")
    game2 = Game("Codenames")
    player = Player("Alice")

    Result(player, game1, 100)
    Result(player, game2, 200)
    Result(player, game1, 150)

    results = player.results()
    games_played = player.games_played()

    assert all(isinstance(r, Result) for r in results)
    assert all(isinstance(g, Game) for g in games_played)
    assert len(games_played) == 2  # unique games

def test_played_game_and_num_times_played():
    game1 = Game("Chess")
    game2 = Game("Checkers")
    player = Player("Bob")

    Result(player, game1, 100)
    Result(player, game1, 200)

    assert player.played_game(game1) is True
    assert player.played_game(game2) is False
    assert player.num_times_played(game1) == 2
    assert player.num_times_played(game2) == 0

def test_highest_scored():
    game = Game("Monopoly")
    player1 = Player("Alice")
    player2 = Player("Bob")

    Result(player1, game, 100)
    Result(player1, game, 300)
    Result(player2, game, 250)
    Result(player2, game, 350)

    highest = Player.highest_scored(game)
    assert highest == player2
