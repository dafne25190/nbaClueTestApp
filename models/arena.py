
from utils.db import db

class Arena(db.Model):
    ARENA_ID = db.Column(db.Integer, primary_key = True, nullable = False)
    Names = db.Column(db.String(100),  nullable = False)
    Capacity = db.Column(db.Integer,  nullable = False)
    
    def __init__(self, arenaId, name, arenaCapacity):
        self.ARENA_ID = arenaId
        self.Names = name
        self.Capacity = arenaCapacity