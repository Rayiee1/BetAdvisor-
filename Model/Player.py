class Player:

    teamID = None
    playerID = None
    playerName = None
    position = None

    avgPts = None
    lowestPts = None
    highestPts = None

    avgReb = None
    lowestReb = None
    highestReb = None

    avgAssist = None
    lowestAssist = None
    highestAssist = None

    avgSteal = None
    lowestSteal= None
    highestSteal= None

    avg3s = None
    lowest3s= None
    highest3s = None

    avgBlock = None
    lowestBlock= None
    highestBlock= None

    injuryStatus = False
    starter = False
    def __init__(self, playerID=None, playerName=None, position=None,
                 avgPts=None, lowestPts=None, highestPts=None,
                 avgReb=None, lowestReb=None, highestReb=None,
                 avgAssist=None, lowestAssist=None, highestAssist=None,
                 avgSteal=None, lowestSteal=None, highestSteal=None,
                 avgBlock=None, lowestBlock=None, highestBlock=None,
                 avg3s=None, lowest3s=None, highest3s=None,
                 injuryStatus=False, starter=False, teamID = None):
        self.playerID = playerID
        self.playerName = playerName
        self.position = position
        self.avgPts = avgPts
        self.lowestPts = lowestPts
        self.highestPts = highestPts
        self.avgReb = avgReb
        self.lowestReb = lowestReb
        self.highestReb = highestReb
        self.avgAssist = avgAssist
        self.lowestAssist = lowestAssist
        self.highestAssist = highestAssist
        self.avgSteal = avgSteal
        self.lowestSteal = lowestSteal
        self.highestSteal = highestSteal
        self.avg3s = avg3s
        self.lowest3s = lowest3s
        self.highest3s = highest3s
        self.avgBlock = avgBlock
        self.lowestBlock = lowestBlock
        self.highestBlock = highestBlock
        self.injuryStatus = injuryStatus
        self.starter = starter
        self.teamID = teamID
    # Getters
    def get_playerID(self):
        return self.playerID

    def get_playerName(self):
        return self.playerName

    def get_position(self):
        return self.position

    def get_avgPts(self):
        return self.avgPts

    def get_lowestPts(self):
        return self.lowestPts

    def get_highestPts(self):
        return self.highestPts

    def get_avgReb(self):
        return self.avgReb

    def get_lowestReb(self):
        return self.lowestReb

    def get_highestReb(self):
        return self.highestReb

    def get_avgAssist(self):
        return self.avgAssist

    def get_lowestAssist(self):
        return self.lowestAssist

    def get_highestAssist(self):
        return self.highestAssist

    def get_avgSteal(self):
        return self.avgSteal

    def get_lowestSteal(self):
        return self.lowestSteal

    def get_highestSteal(self):
        return self.highestSteal

    def get_avg3s(self):
        return self.avg3s

    def get_lowest3s(self):
        return self.lowest3s

    def get_highest3s(self):
        return self.highest3s

    def get_avgBlock(self):
        return self.avgBlock

    def get_lowestBlock(self):
        return self.lowestBlock

    def get_highestBlock(self):
        return self.highestBlock

    def get_injuryStatus(self):
        return self.injuryStatus

    def get_starter(self):
        return self.starter

    # Setters
    def set_playerID(self, playerID):
        self.playerID = playerID

    def set_playerName(self, playerName):
        self.playerName = playerName

    def set_position(self, position):
        self.position = position

    def set_avgPts(self, avgPts):
        self.avgPts = avgPts

    def set_lowestPts(self, lowestPts):
        self.lowestPts = lowestPts

    def set_highestPts(self, highestPts):
        self.highestPts = highestPts

    def set_avgReb(self, avgReb):
        self.avgReb = avgReb

    def set_lowestReb(self, lowestReb):
        self.lowestReb = lowestReb

    def set_highestReb(self, highestReb):
        self.highestReb = highestReb

    def set_avgAssist(self, avgAssist):
        self.avgAssist = avgAssist

    def set_lowestAssist(self, lowestAssist):
        self.lowestAssist = lowestAssist

    def set_highestAssist(self, highestAssist):
        self.highestAssist = highestAssist

    def set_avgSteal(self, avgSteal):
        self.avgSteal = avgSteal

    def set_lowestSteal(self, lowestSteal):
        self.lowestSteal = lowestSteal

    def set_highestSteal(self, highestSteal):
        self.highestSteal = highestSteal

    def set_avg3s(self, avg3s):
        self.avg3s = avg3s

    def set_lowest3s(self, lowest3s):
        self.lowest3s = lowest3s

    def set_highest3s(self, highest3s):
        self.highest3s = highest3s

    def set_avgBlock(self, avgBlock):
        self.avgBlock = avgBlock

    def set_lowestBlock(self, lowestBlock):
        self.lowestBlock = lowestBlock

    def set_highestBlock(self, highestBlock):
        self.highestBlock = highestBlock

    def set_injuryStatus(self, injuryStatus):
        self.injuryStatus = injuryStatus

    def set_starter(self, starter):
        self.starter = starter
    def get_teamID(self):
        return self.teamID
    def set_teamID(self, teamID):
        self.teamID = teamID