from db import db, connection, metadata, engine, Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = 'TASKS'
    
    task_id = db.Column(db.Integer, primary_key=True, index=True)
    task_is_done = db.Column(db.Boolean, nullable=False)
    task_is_termless = db.Column(db.Boolean, nullable=False)
    task_name = db.Column(db.Text, nullable=False)
    task_description = db.Column(db.Text, nullable=True)
    task_date = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer)
    
Base.metadata.create_all(bind=engine)