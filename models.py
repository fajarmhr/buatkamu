from datetime import datetime
from pytz import timezone
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

UTC = timezone('Asia/Jakarta')

def time_now():
    return datetime.now(UTC)
 
class SurveyModel(db.Model):
    __tablename__ = "sepikann"
 
    id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String())
    nick = db.Column(db.String())
    syg = db.Column(db.String())
    time_created = db.Column(db.DateTime(timezone=True), default=time_now)
 
    def __init__(self, name,nick,syg):
        self.name = name
        self.nick = nick
        self.syg = syg
 
    def __repr__(self):
        return f"{self.nick}:{self.name}"