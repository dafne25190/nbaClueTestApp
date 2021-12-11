from flask import Blueprint, render_template
from utils.createDatabase import CreateDB 

nbaTest = Blueprint('nbaTest',__name__)

@nbaTest.route('/')
def home():
    CreateDB()
    return render_template('index.html')

@nbaTest.route('/prediction')
def view_prediction():
    return "1 player"
