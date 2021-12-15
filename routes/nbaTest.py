from flask import Blueprint, render_template, request, flash
from utils.createDatabase import createDataBase 
from utils.prediction import  prediction, getAllTeams
from models.games import Games
from utils.db import db
from utils.best_player import best_player, all_season
import pandas as pd
import numpy as np

nbaTest = Blueprint('nbaTest',__name__)

@nbaTest.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('Entre')
        flash("Esto puede tomar unos minutos ...")
        createDataBase()
        flash ("Se ha creado la Base de Datos")
    return render_template('index.html')

@nbaTest.route('/best_player', methods=['GET', 'POST'])
def give_best_player():
    bp = []
    seasons = all_season()
    if request.method == "POST":
        season = int(request.form["seasons"])
        bp = best_player(season)
    return render_template('best_player.html', bestPlayers = bp, seasons = seasons)

@nbaTest.route('/prediction', methods=['GET', 'POST'])
def view_prediction():
    winner = ''
    all_teams = getAllTeams()
    if request.method == "POST":
        home_team = int(request.form["home_team"])
        away_team = int(request.form["away_team"])
        winner = prediction(home_team, away_team)
    return render_template('prediction.html', winner = winner, all_teams = all_teams)
