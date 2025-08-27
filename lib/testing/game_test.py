# test_game.py
import pytest
from ..classes.many_to_many import Game, Player, Result


@pytest.fixture(autouse=True)
def reset_class_lists():
    # Reset class-level lists before each test
    Game.all_games = []
    Player.all_players = []
    Result.all = []

def test_game_initialization():
    game = Game("Skribbl.io")
    assert game.title == "Skribbl.io"
    assert isinstance(game.title, str)

def test_title_is_immutable():
    game = Game("Codenames")
    with pytest.raises(AttributeError):
        game.title = "New Game"

def test_game_results_and_players():
    game = Game("Skribbl.io")
    player1 = Player("Alice")
    player2 = Player("Bob")

    Result(player1, game, 2000)
    Result(player2, game, 3000)
    Result(player1, game, 2500)

    results = game.results()
    players = game.players()

    assert all(isinstance(r, Result) for r in results)
    assert all(isinstance(p, Player) for p in players)
    assert len(players) == 2  # unique players

def test_average_score():
    game = Game("Chess")
    player = Player("Alice")

    Result(player, game, 100)
    Result(player, game, 300)
    Result(player, game, 200)

    avg = game.average_score(player)
    assert avg == 200
