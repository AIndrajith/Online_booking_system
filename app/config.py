import os
from dotenv import load_dotenv

load_dotenv()

pg_username = os.getenv('POSTGRES_USER_NAME')
pg_password = os.getenv('POSTGRES_PASSWORD')
pg_database = os.getenv('POSTGRES_DB')
pg_port = os.getenv('DB_PORT')
pg_host = os.getenv('DB_HOST')
pg_connection = os.getenv('DB_CONNECTION')

SQLALCHEMY_DATABASE_URL = f"{pg_connection}://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
print("pg_url => ",SQLALCHEMY_DATABASE_URL)