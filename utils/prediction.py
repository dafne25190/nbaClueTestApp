from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from models.games import Games
from models.teams import Teams
from utils.db import db

def prediction(team1Id, team2Id):
    current = db.session.query(Games)

    games = pd.read_sql_query(current.statement, db.engine)

    games = games.dropna()
    FIELDS_TO_DROP = ['PTS_home', 'PTS_away','HOME_TEAM_WINS', 'GAME_DATE_EST', 'GAME_STATUS_TEXT',
                  'SEASON', 'GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID']

    X = games.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
    y = games[['PTS_home', 'PTS_away']].values

    #Select only match between to teams
    df_new = games[games['HOME_TEAM_ID'] == team1Id]
    df_new = df_new[df_new['VISITOR_TEAM_ID'] == team2Id]

    #Sort By Recent Season
    df_new = df_new.sort_values(by=['SEASON'], ascending=False)
    df_new.head()

    FIELDS_TO_APPLIED_KDE = ['FG_PCT_home', 'FT_PCT_home','FG3_PCT_home', 'AST_home', 'REB_home',
                  'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away',  'AST_away',  'REB_away'  ]
    
    df = simulate_games(df_new, FIELDS_TO_APPLIED_KDE)
    prediction = rfr_Prediction(X, y, df)
    winner = obtain_winner(prediction)
    winnerId = ''
    if (winner == 0): winnerId = team1Id 
    else: winnerId = team2Id

    winner = db.session.query(Teams.NICKNAME).filter(Teams.TEAM_ID == winnerId).first()
    return winner[0]

def create_KDE_data(values):
    data = np.hstack((values.array))
    ponderate_value = []
    total = len(data)
    for i in data:
        ponderate_value.extend([i]*total)
        total = total -1
    return np.hstack(ponderate_value)

def kde_model(ponderate_value):
    param_grid = {'kernel': ['gaussian', 'tophat'],
              'bandwidth' : np.linspace(0.01, 3, 10)
             }

    grid = GridSearchCV(
        estimator  = KernelDensity(),
        param_grid = param_grid,
        n_jobs     = -1,
        cv         = 10, 
        verbose    = 0
      )

    _ = grid.fit(X = ponderate_value.reshape((-1,1)))
    modelo_kde_final = grid.best_estimator_
    prediction = []
    for i in range(1,30):
        value = modelo_kde_final.sample()
        prediction.append(value[0][0])
    return prediction
    
def simulate_games(data, FIELDS_TO_APPLIED_KDE):
    df = pd.DataFrame()
    for name in FIELDS_TO_APPLIED_KDE:
        values = data[name]
        kde_data = create_KDE_data(values)
        prediction_values = kde_model(kde_data)
        df[name] = prediction_values 
    return df

def rfr_Prediction(X_train,y_train, X_test):
    parameters = {'bootstrap': False,
                  'min_samples_leaf': 3,
                  'n_estimators': 50,
                  'min_samples_split': 10,
                  'max_features': 'sqrt',
                  'max_depth': 6}
    model = RandomForestRegressor(**parameters)
    model.fit(X_train, y_train)
    return model.predict(X_test).astype(int)

def obtain_winner(prediction):
    print(prediction)
    first_team = sum(x[0] > x[1] for x in prediction)
    print(first_team)
    if(len(prediction)/2>first_team): return 1 
    else: return 0

def getAllTeams ():
    teams = db.session.query(Teams.TEAM_ID, Teams.NICKNAME).order_by(Teams.NICKNAME).distinct(Teams.TEAM_ID).all()
    return teams
