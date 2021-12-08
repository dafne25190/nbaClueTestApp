from flask import Blueprint, render_template

players = Blueprint('players',__name__)

@players.route('/')
def home():
    return render_template('index.html')

@players.route('/players')
def view_players():
    return "1 player"
