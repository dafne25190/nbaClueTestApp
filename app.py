from flask import Flask
from routes.players import players

app = Flask(__name__)
  
app.register_blueprint(players)

 