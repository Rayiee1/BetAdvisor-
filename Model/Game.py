class Game:
    home_Team = None
    away_Team = None
    gameID = None


    def __init__(self, home_Team, away_Team, gameID):
        self.home_Team = home_Team
        self.away_Team = away_Team
        self.gameID = gameID
    def getHomeTeam(self):
        return self.home_Team
    def setHomeTeam(self, home_Team):
        self.home_Team = home_Team
    def getAwayTeam(self):
        return self.away_Team
    def setAwayTeam(self, away_Team):
        self.away_Team = away_Team
    def getGameID(self):
        return self.gameID
    def setGameID(self, gameID):
        self.gameID = gameID