
from utils.db import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    game = db.Column(db.String(20), nulleable = False)
    
    def __init__(self, game):
        self.game = game