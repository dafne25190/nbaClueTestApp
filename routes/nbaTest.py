from flask import Blueprint, render_template
from utils.createDatabase import createDataBase 
from utils.prediction import  prediction
from models.games import Games
from utils.db import db
from utils.best_player import best_player
import pandas as pd
import numpy as np

nbaTest = Blueprint('nbaTest',__name__)

@nbaTest.route('/')
def home():
    # createDataBase()
    return render_template('index.html')

@nbaTest.route('/best_player')
def give_best_player():
    bp = best_player(2020)
    return "yo"

@nbaTest.route('/prediction')
def view_prediction():
    winner = prediction(1610612762, 1610612742)
    return winner
