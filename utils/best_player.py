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
    query = "Select week, players.Names, prod from ( Select week, T.PLAYER_ID, max(T.productivity) as prod From (SELECT gamesplayer.PLAYER_ID, WEEK(games.GAME_DATE_EST) as week, (sum(gamesplayer.REB) +sum(gamesplayer.PTS) + sum(gamesplayer.AST)) as productivity FROM gamesplayer join games on gamesplayer.GAME_ID = games.GAME_ID WHERE games.SEASON = :season GROUP by week, PLAYER_ID) as T GROUP by week) as new JOIN players on players.PLAYER_ID = new.PLAYER_ID"
    result = connection.execute(text(query), season = season)
    result_dict = result.mappings().all()
    print(result_dict)
    return result
