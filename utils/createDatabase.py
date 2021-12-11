from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONNECTION_URI
from models.teams import Teams
import pandas as pd
from utils.db import db
import os
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
    return True
    
def createTable (all_datas, name):
    df = all_datas[name]
    for i in len(df):
        current_cell = df.iloc[i]
        record = Teams(tuple(current_cell)) #use eval()
        db.session.add(record) #Add all the records
        db.session.commit() #Attempt to commit all the records

def createDataBase (all_data):
    for key in all_data:
        createTable(all_data,key)
    
    
        
        