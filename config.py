from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
psw = os.environ['MYSQL_PSW']
host = os.environ['MYSQL_HOST']
db_name = os.environ['MYSQL_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}@{host}/{db_name}'
