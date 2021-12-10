
from utils.db import db

class Teams(db.Model):
    teamId = db.Column(db.Integer, primary_key = True)
    leagueId = db.Column(db.Integer)
    minYear = db.Column(db.Interger)
    maxYear = db.Column(db.Interger)
    city = db.Column(db.String(20))
    
    def __init__(self, teamId, leagueID, minYear,maxYear, city):
        self.teamId = teamId
        self.leagueId = leagueID
        self.minYear = minYear
        self.maxYear = maxYear
        self.city = city

  