
from utils.db import db
from models.arena import Arena
from models.city import City

class Teams(db.Model):
    TEAM_ID = db.Column(db.Integer, primary_key = True)
    MIN_YEAR = db.Column(db.Integer)
    MAX_YEAR = db.Column(db.Integer)
    ABBREVIATION = db.Column(db.String(100), nullable = False)
    NICKNAME = db.Column(db.String(100), nullable = False)
    
    CITY_ID = db.Column(db.Integer, db.ForeignKey(City.CITY_ID), nullable = False)
    # city = db.relationship("City", back_populates = 'City')
    
    ARENA_ID = db.Column(db.Integer, db.ForeignKey(Arena.ARENA_ID) , nullable = False)
    # arena = db.relationship("Arena", back_populates = 'Arena')

    OWNER = db.Column(db.String(100), nullable = False)
    GENERALMANAGER = db.Column(db.String(100), nullable = False)
    HEADCOACH = db.Column(db.String(100), nullable = False)
    DLEAGUEAFFILIATION = db.Column(db.String(100), nullable = False)
    
    
    def __init__(self, teamId, minYear, maxYear,abbreviation,nickname, cityId, arenaId, owner, generalManager, headCoach, dLeagueAffiliation):
        self.TEAM_ID = teamId
        self.MIN_YEAR = minYear
        self.MAX_YEAR = maxYear
        self.ABBREVIATION = abbreviation
        self.NICKNAME = nickname
        self.CITY_ID = cityId
        self.ARENA_ID = arenaId
        self.GENERALMANAGER = generalManager
        self.OWNER = owner
        self.HEADCOACH = headCoach
        self.DLEAGUEAFFILIATION = dLeagueAffiliation

  