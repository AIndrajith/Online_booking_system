from app.db.postgresDB import engine, Base
import app.models.pg_models

def init_models():
    Base.metadata.create_all(bind=engine)