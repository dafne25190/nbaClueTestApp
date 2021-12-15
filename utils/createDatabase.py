from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONNECTION_URI

import pandas as pd
import numpy as np
from utils.db import db
import os

from models.arena import Arena
from models.city import City
from models.conference import Conference
from models.games import Games
from models.gamesPlayer import GamesPlayer
from models.playerTeam import PlayerTeam
from models.players import Players
from models.ranking import Ranking
from models.teams import Teams

data_path = os.environ['DATA_PATH']


Base = declarative_base()

def load_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        data_df = pd.read_csv(file)
        return data_df

def readAllData(data_path):
    all_files = os.listdir(data_path)
    all_datas = {}
    for file in all_files:
        all_datas[file.split('.')[0]] = load_csv(data_path +'/' + file) 
    return all_datas

def normalizeData(all_datas):
     
    teams_df = all_datas['teams']
    ranking_df = all_datas['ranking']
    games_df = all_datas['games']

    #Delete duplicate columns
    teams_df.drop('YEARFOUNDED', axis=1, inplace=True)
    games_df.drop(['TEAM_ID_home', 'TEAM_ID_away'], axis=1, inplace=True)

    #Delete unnecessary columns
    games_player_df = all_datas['games_details']
    games_player_df.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_NAME'], axis=1, inplace=True)
    teams_df.drop('LEAGUE_ID', axis=1, inplace=True)
    ranking_df.drop('LEAGUE_ID', axis=1, inplace=True)

    #create auxiliary tables
    teams_df, city_df = createCity(teams_df)
    teams_df, arena_df = createArena(teams_df)
    
    ranking_df, conference_df = createConference(ranking_df)

    players_team_df = all_datas['players']
    players_team_df, player_df = createPlayer(players_team_df)

    #atomic values
    ranking_df['HOME_RECORD_W'] = ranking_df['HOME_RECORD'].str[0]
    ranking_df['HOME_RECORD_L'] = ranking_df['HOME_RECORD'].str[2]
    ranking_df['ROAD_RECORD_W'] = ranking_df['ROAD_RECORD'].str[0]
    ranking_df['ROAD_RECORD_L'] = ranking_df['ROAD_RECORD'].str[2]
    ranking_df.drop('HOME_RECORD', axis=1, inplace=True)
    ranking_df.drop('ROAD_RECORD', axis=1, inplace=True)
    ranking_df.drop('TEAM', axis=1, inplace=True)

    result = {
        'Arena': arena_df,
        'City': city_df,
        'Conference': conference_df,
        'Teams' : teams_df,
        'Players': player_df,
        'GamesPlayer': games_player_df,
        'Games': games_df,
        'PlayerTeam': players_team_df,
        'Ranking': ranking_df
        
    }

    index = {
        'Arena': True,
        'City': True,
        'Conference': True,
        'Teams' : False,
        'Players': True,
        'GamesPlayer': False,
        'Games': False,
        'PlayerTeam': False,
        'Ranking': False,
        
    }

    return (result,index)


def expandTables(table, uniqueValues, currentColumnName, newColumnName):
    newTable = pd.DataFrame(uniqueValues, columns = [newColumnName])
    newTable.index = np.arange(1, len(newTable)+1)
    ids = []
    for value in table[currentColumnName]:
        ids.extend(newTable.index[newTable[newColumnName] == value])

    table[currentColumnName] = ids
    table = table.rename(columns={currentColumnName: currentColumnName+'_ID'})
    newTable = newTable.rename_axis(currentColumnName+'_ID')
    return (table, newTable)

def createCity(teams_df):
    uniqueValues = teams_df['CITY'].unique()
    return expandTables(teams_df, uniqueValues, 'CITY', 'Names')

def createArena(teams_df):
    teams_df['ARENACAPACITY'] = teams_df['ARENACAPACITY'].fillna(0)
    teams_df['ARENA'] = teams_df[['ARENA', 'ARENACAPACITY']].to_records(index=False)

    uniqueValues = (teams_df['ARENA']).unique()
    
    teams_df, arena_df = expandTables(teams_df, uniqueValues, 'ARENA', 'tuple')
    
    arena_df['Names'], arena_df['Capacity'] = arena_df['tuple'].str
    arena_df.drop('tuple', axis=1, inplace=True)
    teams_df.drop('ARENACAPACITY', axis=1, inplace=True)
   
    return (teams_df, arena_df)

def createConference(ranking_df):
    uniqueValues = ranking_df['CONFERENCE'].unique()
    return expandTables(ranking_df, uniqueValues, 'CONFERENCE', 'Names')

def createPlayer(players_team_df):
    players_team_df['tuple'] = list(players_team_df[['PLAYER_ID', 'PLAYER_NAME']].to_records(index=False))
    uniqueValues = players_team_df['tuple'].apply(lambda x: eval(str(x))).unique()
   
    player_df = pd.DataFrame(uniqueValues, columns = ['Names'])
    player_df['PLAYER_ID'], player_df['Names'] = player_df['Names'].str
    player_df = player_df.set_index('PLAYER_ID')
    players_team_df.drop('PLAYER_NAME', axis=1, inplace=True)
    players_team_df.drop('tuple', axis=1, inplace=True)
    return (players_team_df, player_df)

def createDataBase ():
    all_datas = readAllData(data_path)
    (dataBaseData, index) = normalizeData(all_datas)
    for key in dataBaseData:
        dataBaseData[key].to_sql(name=key.lower(), con=db.engine, index=index[key], if_exists='append')
    
    
        
        