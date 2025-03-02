import json
import os
import _mysql_connector
import mysql
from nba_api.stats.endpoints._base import Endpoint
from Model import Team
from Model import Game
from nba_api.stats.static.teams import find_teams_by_full_name
from nba_api.stats.endpoints import (
    CommonTeamRoster,
    playerdashboardbyteamperformance,
    playergamelog
)



with open("TempData.txt", "r") as f:
    jsonData = json.load(f)

""""
mydb = mysql.connector.connect(
    host= os.environ.get('host'),
    user= os.environ.get('user'),
    password= os.environ.get('password'),
    database = os.environ.get('database')
)
mycursor = mydb.cursor()


def getPlayerIds(TeamName):
    TeamDetail = find_teams_by_full_name(TeamName)
    TeamID = TeamDetail[0]['id']
    TeamRoster = json.loads(CommonTeamRoster(team_id=TeamID).get_json())    #gets roster
    PlayerIds  = []
    headers = TeamRoster['resultSets'][0]['headers']
    player_id_index = headers.index('PLAYER_ID')
    sql = "INSERT INTO TEAM (teamID, teamName) VALUES (%s, %s)"
    val = (TeamID, TeamName)
    mycursor.execute(sql, val)
    for Player in TeamRoster['resultSets'][0]['rowSet']:  #gets every player ID on the roster
        PlayerIds.append(Player[player_id_index])
    getPlayerStats(PlayerIds,TeamID)
    
def gameDetail(JsonData):
    for i in jsonData:
        gameId = i['id']
        homeTeamName = i['home_team']
        awayTeamName = i['away_team']
        awayTeamDetail = find_teams_by_full_name(awayTeamDetail)
        homeTeamDetail = find_teams_by_full_name(homeTeamDetail)
        homeTeamID = homeTeamDetail[0]['id']
        awayTeamID = awayTeamDetail[0]['id']
        sql = "INSERT INTO Games (homeTeamID, awayTeamID, gameID) VALUES (%s, %s, %s)"
        val = (homeTeamID, awayTeamID, gameId)
        mycursor.execute(sql, val)
        getPlayerIds(homeTeamName)
        getPlayerIds(awayTeamName)

def getPlayerStats(PlayerIds, TeamID):

"""

TeamName = jsonData[0]['away_team']
TeamDetail = find_teams_by_full_name(TeamName)
TeamID = TeamDetail[0]['id']
TeamRoster = json.loads(CommonTeamRoster(team_id=TeamID).get_json())    #gets roster
PlayerIds  = []
headers = TeamRoster['resultSets'][0]['headers']
player_id_index = headers.index('PLAYER_ID')

for Player in TeamRoster['resultSets'][0]['rowSet']:  #gets every player ID on this roster and puts it into a list
    PlayerIds.append(Player[player_id_index])



temp = json.loads(playergamelog.PlayerGameLog(player_id=PlayerIds[0]).get_json())
gameLogHeaders = temp['resultSets'][0]['headers']
FGM = gameLogHeaders.index('FGM')
FG3M = gameLogHeaders.index('FG3M')
REB = gameLogHeaders.index('REB')
AST = gameLogHeaders.index('AST')
STL = gameLogHeaders.index('STL')
BLK = gameLogHeaders.index('BLK')



for i in PlayerIds: #for every player get game log
    gameLog = json.loads(playergamelog.PlayerGameLog(player_id=PlayerIds[i]).get_json())
    thisPlayerFGM = []
    thisPlayerFG3M = []
    thisPlayerREB = []
    thisPlayerAST = []
    thisPlayerSTL = []
    thisPlayerBLK = []

    for Games in gameLog['resultSets'][0]['rowSet']: #for every rowset in gamelogs add the stat into the list of this player
        thisPlayerFGM.append(Games[FGM])
        thisPlayerFG3M.append(Games[FG3M])
        thisPlayerREB.append(Games[REB])
        thisPlayerAST.append(Games[AST])
        thisPlayerSTL.append(Games[STL])
        thisPlayerBLK.append(Games[BLK])

    thisPlayerFGM.sort()
    thisPlayerFG3M.sort()
    thisPlayerREB.sort()
    thisPlayerAST.sort()
    thisPlayerSTL.sort()
    thisPlayerBLK.sort()

print(temp)
