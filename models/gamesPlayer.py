
from utils.db import db
from models.players import Players
from models.teams import Teams

class GamesPlayer(db.Model):
    GAME_ID = db.Column(db.Integer, primary_key = True)	 
    PLAYER_ID = db.Column(db.Integer, db.ForeignKey(Players.PLAYER_ID), primary_key = True)
    TEAM_ID	= db.Column(db.Integer, db.ForeignKey(Teams.TEAM_ID))
    START_POSITION = db.Column(db.String(5))	 
    COMMENT	 = db.Column(db.String(50))	 
    MIN	= db.Column(db.String(20))	 	 
    FGM	= db.Column(db.Integer)	 
    FGA	= db.Column(db.Integer)	 
    FG_PCT	= db.Column(db.Float)	 
    FG3M	= db.Column(db.Integer)	 
    FG3A	= db.Column(db.Integer)	 
    FG3_PCT	= db.Column(db.Float)	 
    FTM	= db.Column(db.Integer)		 
    FTA	= db.Column(db.Integer)		 
    FT_PCT	= db.Column(db.Float)	 
    OREB	= db.Column(db.Integer)		 
    DREB	= db.Column(db.Integer)		 
    REB	= db.Column(db.Integer)		 
    AST	= db.Column(db.Integer)		 
    STL	= db.Column(db.Integer)		 
    BLK	= db.Column(db.Integer)		 
    TO	= db.Column(db.Integer)		 
    PF	= db.Column(db.Integer)		 
    PTS	= db.Column(db.Integer)		 
    PLUS_MINUS	= db.Column(db.Integer)	

    def __init__(self, game_id, player_id, team_id, start_position, comment, min, fgm, fga, fg_pct, fg3m, fg3a,
                fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, to, pf, pts, plus_minus):
        self.GAME_ID = game_id 	 
        self.PLAYER_ID = player_id 
        self.TEAM_ID = team_id
        self.START_POSITION = start_position 	 
        self.COMMENT = comment
        self.MIN = min	 	 
        self.FGM = fgm	
        self.FGA = fga	
        self.FG_PCT = fg_pct	 
        self.FG3M = fg3m
        self.FG3A = fg3a	
        self.FG3_PCT = fg3_pct	 
        self.FTM = ftm	 
        self.FTA = fta	
        self.FT_PCT = ft_pct	 
        self.OREB = oreb		 
        self.DREB = dreb	 
        self.REB = reb		 
        self.AST = ast		 
        self.STL = stl		 
        self.BLK = blk		 
        self.TO = to	 
        self.PF = pf		 
        self.PTS = pts		 
        self.PLUS_MINUS = plus_minus