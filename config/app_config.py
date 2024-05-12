# Flask secret key
import secrets

SECRET_KEY = secrets.token_hex(16)

# Database URI
DATABASE = 'mysql+pymysql'
USERNAME = 'root'
PASSWORD = '123123'
# Change address from 127.0.0.1 to db (compose.yaml)
ADDRESS = 'db'
PORT = 3306
DATABASE_NAME = 'simritest'
