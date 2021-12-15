
from utils.db import db
from models.conference import Conference
from models.teams import Teams

class Ranking(db.Model):
    TEAM_ID = db.Column(db.Integer, db.ForeignKey(Teams.TEAM_ID), primary_key = True)
    SEASON_ID = db.Column(db.Integer, primary_key = True)
    STANDINGSDATE = db.Column(db.Date, primary_key = True)
    CONFERENCE_ID = db.Column(db.Integer, db.ForeignKey(Conference.CONFERENCE_ID), nullable = False)
    conference = db.relationship("Conference", backref=db.backref("conference", uselist=False))
    G = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    W_PCT = db.Column(db.Float)
    HOME_RECORD_W = db.Column(db.Integer)
    HOME_RECORD_L = db.Column(db.Integer)
    ROAD_RECORD_W = db.Column(db.Integer)
    ROAD_RECORD_L = db.Column(db.Integer)
    RETURNTOPLAY = db.Column(db.Boolean)
    
    
    def __init__(self, teamId, seasonId, standingDate,conferenceId,games, wins, loses, w_pct, homeRecorW, homeRecordL, roadRecordW, roadRecordL, returnToPlay):
        self.TEAM_ID = teamId
        self.SEASON_ID = seasonId
        self.STANDINGSDATE = standingDate
        self.CONFERENCE_ID = conferenceId
        self.G = games
        self.W = wins
        self.L = loses
        self.W_PCT = w_pct
        self.RETURNTOPLAY = returnToPlay
        self.HOME_RECORD_L = homeRecordL
        self.HOME_RECORD_W = homeRecorW
        self.ROAD_RECORD_L = roadRecordL
        self.ROAD_RECORD_W = roadRecordW

  