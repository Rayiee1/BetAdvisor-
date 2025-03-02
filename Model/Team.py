
class Team :
    teamID = None
    Players = []
    teamName = None
    def __init__(self, teamID=None, players=None, teamName=None):
        self.teamID = teamID
        self.players = players
        self.teamName = teamName

# Getters
    def get_teamID(self):
        return self.teamID

    def get_players(self):
        return self.players

    def get_teamName(self):
        return self.teamName

    # Setters
    def set_teamID(self, teamID):
        self.teamID = teamID

    def set_players(self, players):
        self.players = players

    def set_teamName(self, teamName):
        self.teamName = teamName


