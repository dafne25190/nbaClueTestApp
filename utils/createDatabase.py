from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONNECTION_URI
from models.teams import Teams
import pandas as pd
from utils.db import db

Base = declarative_base()

def load_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        data_df = pd.read_csv(file)
        return data_df

class CreateDB:
    def __init__(self):
            print('here3')
            teams_df = load_csv('./nbaData/teams.csv') 
            for ind in teams_df.index:
                leagueId =  teams_df['LEAGUE_ID'][ind]
                teamId = teams_df['TEAM_ID'][ind]
                minYear = teams_df['MIN_YEAR'][ind]
                maxYear = teams_df['MAX_YEAR'][ind]
                city = teams_df['CITY'][ind]
                record = Teams(teamId,leagueId,minYear,maxYear,city)
                db.session.add(record) #Add all the records

            db.session.commit() #Attempt to commit all the records
        