
from utils.db import db

class Players(db.Model):
    PLAYER_ID = db.Column(db.Integer, primary_key = True)
    Names = db.Column(db.String(100), nullable = False)
    
    def __init__(self, playerId, name):
        self.PLAYER_ID = playerId
        self.Names = name