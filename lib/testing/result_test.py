import pytest
from lib.classes.many_to_many import Game, Player, Result

class TestResults:
    def test_result_is_initialized_with_score(self):
        """Result is initialized with a score"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 2000)
        assert result.score == 2000

    def test_score_is_immutable_int(self):
        """Result score is an immutable integer"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result_1 = Result(player, game, 2000)

        assert isinstance(result_1.score, int)

        # Expect AttributeError when trying to set a new score
        with pytest.raises(AttributeError):
            result_1.score = 5000

    def test_score_in_range(self):
        """Score is between 1 and 5000 inclusive"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 1)
        assert 1 <= result.score <= 5000

        result = Result(player, game, 5000)
        assert 1 <= result.score <= 5000

    def test_result_has_player(self):
        """Result has a player"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 2000)
        assert result.player == player

    def test_result_has_game(self):
        """Result has a game"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 2000)
        assert result.game == game
