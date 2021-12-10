from flask import Blueprint, render_template
# from models.players import Players

players = Blueprint('players',__name__)

@players.route('/')
def home():
    # players = Players.query.all()
    return render_template('index.html', players = players)

@players.route('/players')
def view_players():
    return "1 player"
