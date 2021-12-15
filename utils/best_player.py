from utils.db import db 
from models.games import Games
from models.gamesPlayer import GamesPlayer
from models.playerTeam import Players
from models.teams import Teams
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def best_player(season):
    season_str = str(season)
    connection = db.session.connection()
    query = "Select week, PLAYER_ID, max(productivity) From (SELECT PLAYER_ID, WEEK(Games.GAME_DATE_EST) as week, (sum(GamesPlayer.REB) +sum(GamesPlayer.PTS) + sum(GamesPlayer.AST)) as productivity FROM GamesPlayer join Games on GamesPlayer.GAME_ID = Games.GAME_ID WHERE Games.SEASON = :season GROUP by week, PLAYER_ID) as T GROUP by week"
    result = connection.execute(text(query), season = season)
    result_dict = result.mappings().all()
    print(result_dict)
    return result
