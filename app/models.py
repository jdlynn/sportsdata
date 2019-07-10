from flask import current_app, url_for
from app import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    team= db.Column(db.String(64), index=True)
    position = db.Column(db.String(10))
    age = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    jersey = db.Column(db.Integer)
    photoURL = db.Column(db.String(100))
    initialVal = db.Column(db.Integer)