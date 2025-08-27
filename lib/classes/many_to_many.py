class Game:
    all_games = []

    def __init__(self, title: str):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = title
        Game.all_games.append(self)

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        unique_players = []
        for result in self.results():
            if result.player not in unique_players:
                unique_players.append(result.player)
        return unique_players

    def average_score(self, player):
        player_results = [r.score for r in self.results() if r.player == player]
        if not player_results:
            return 0
        return sum(player_results) / len(player_results)


class Player:
    all_players = []

    def __init__(self, username: str):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be 2-16 characters")
        self._username = username
        Player.all_players.append(self)

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return isinstance(other, Player) and self.username == other.username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str) or not (2 <= len(new_username) <= 16):
            raise ValueError("Username must be 2-16 characters")
        self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_games = []
        for result in self.results():
            if result.game not in unique_games:
                unique_games.append(result.game)
        return unique_games

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        highest_player = None
        highest_avg = 0
        for player in cls.all_players:
            avg = game.average_score(player)
            if avg > highest_avg:
                highest_avg = avg
                highest_player = player
        return highest_player


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise ValueError("player must be a Player instance")
        if not isinstance(game, Game):
            raise ValueError("game must be a Game instance")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("score must be an int between 1 and 5000")

        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
