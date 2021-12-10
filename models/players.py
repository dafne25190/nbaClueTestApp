
from _typeshed import Self
from utils.db import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    playerName = db.Column(db.String(20), nulleable = False)
    
    def __init__(self, name):
        self.playerName = name