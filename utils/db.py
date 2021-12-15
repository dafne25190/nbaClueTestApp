from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

db = SQLAlchemy()

# SQLALCHEMY_ENGINE_OPTIONS = {
#     'pool': None,
#     'pool_size': 10,
#     'pool_recycle': 120,
#     'pool_pre_ping': True
# }
# engine = db.create_engine(DATABASE_CONNECTION_URI, SQLALCHEMY_ENGINE_OPTIONS)