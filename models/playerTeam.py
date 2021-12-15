
from utils.db import db
from models.players import Players
from models.teams import Teams

class PlayerTeam(db.Model):
    PLAYER_ID = db.Column(db.Integer, db.ForeignKey(Players.PLAYER_ID), nullable = False, primary_key = True)
    TEAM_ID = db.Column(db.Integer, db.ForeignKey(Teams.TEAM_ID), nullable = False, primary_key = True) 
    SEASON = db.Column(db.Integer)
    
    def __init__(self, playerId, teamId, season):
        self.PLAYER_ID = playerId
        self.TEAM_ID = teamId
        self.SEASON = season