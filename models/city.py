
from utils.db import db

class City(db.Model):
    CITY_ID = db.Column(db.Integer, primary_key = True)
    Names = db.Column(db.String(100), nullable = False)
    
    def __init__(self, cityId, name):
        self.CITY_ID = cityId
        self.Names = name