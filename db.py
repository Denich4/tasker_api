import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase

db = db
engine = db.create_engine('sqlite:///tasker_db.db')
connection = engine.connect()
metadata = db.MetaData()

class Base(DeclarativeBase): pass

def get_connection():
    return connection

def get_metadata():
    return metadata

def get_engine():
    return engine

def get_db():
    return db