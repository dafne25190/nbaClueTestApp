
from utils.db import db
from models.teams import Teams

class Games(db.Model):
    GAME_ID = db.Column(db.Integer, primary_key = True)
    GAME_DATE_EST = db.Column(db.Date, nullable = False)
    GAME_STATUS_TEXT = db.Column(db.String(20))
  
    HOME_TEAM_ID = db.Column(db.Integer, db.ForeignKey(Teams.TEAM_ID), nullable = False)
    VISITOR_TEAM_ID = db.Column(db.Integer, db.ForeignKey(Teams.TEAM_ID), nullable = False)

    SEASON = db.Column(db.Integer)
    PTS_home = db.Column(db.Integer)
    FG_PCT_home	= db.Column(db.Float)	 
    FT_PCT_home	= db.Column(db.Float)	 
    FG3_PCT_home = db.Column(db.Float)	 
    AST_home = db.Column(db.Integer)	 
    REB_home = db.Column(db.Integer)	 
    PTS_away = db.Column(db.Integer)	 
    FG_PCT_away	= db.Column(db.Float)	 
    FT_PCT_away	= db.Column(db.Float)	 
    FG3_PCT_away = db.Column(db.Float)	 
    AST_away = db.Column(db.Integer)	 
    REB_away = db.Column(db.Integer)	 
    HOME_TEAM_WINS = db.Column(db.Boolean)
    
    def __init__(self, id, game_date_est, game_status_text, home_team_id, visitor_team_id, season, 
                    pts_home, fg_pct_home, ft_pct_home, fg3_pct_home, ast_home, reb_home, pts_away, 	 
                    fg_pct_away, ft_pct_away, fg3_pct_away, ast_away, reb_away, home_team_wins):
        self.GAME_ID= id	 
        self.GAME_DATE_EST = game_date_est
        self.GAME_STATUS_TEXT = game_status_text	 
        self.HOME_TEAM_ID = home_team_id	 
        self.VISITOR_TEAM_ID = visitor_team_id	 
        self.SEASON = season	 
        self.PTS_home = pts_home	 
        self.FG_PCT_home = fg_pct_home	 
        self.FT_PCT_home = ft_pct_home	 
        self.FG3_PCT_home = fg3_pct_home	 
        self.AST_home = ast_home	 
        self.REB_home = reb_home	 
        self.PTS_away = pts_away	 
        self.FG_PCT_away = fg_pct_away	 
        self.FT_PCT_away = ft_pct_away	 
        self.FG3_PCT_away = fg3_pct_away	 
        self.AST_away = ast_away	 
        self.REB_away = reb_away	 
        self.HOME_TEAM_WINS = home_team_wins