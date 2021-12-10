from flask import Blueprint, render_template
from models.teams import Teams
from utils.db import db
from utils.readNBAData import teams_df
from utils.createDatabase import CreateDB 

players = Blueprint('players',__name__)

@players.route('/')
def home():
    
    return render_template('index.html')

@players.route('/players')
def view_players():
    CreateDB()
    return "1 player"
