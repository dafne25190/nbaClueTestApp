
from utils.db import db

class Conference(db.Model):
    CONFERENCE_ID = db.Column(db.Integer, primary_key = True)
    Names = db.Column(db.String(100), nullable = False)
    
    def __init__(self, conferenceId, name):
        self.CONFERENCE_ID = conferenceId
        self.Names = name