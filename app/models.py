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

class Projection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stockID = db.Column(db.Integer, index=True)
    passingYards = db.Column(db.Float)
    passingInterceptions = db.Column(db.Float)
    rushingAttempts = db.Column(db.Float)
    rushingYards = db.Column(db.Float)
    rushingTouchdowns = db.Column(db.Float)
    receptions = db.Column(db.Float)
    receivingYards = db.Column(db.Float)
    receivingTDs = db.Column(db.Float)
    fumblesLost = db.Column(db.Float)
    puntReturnTDs = db.Column(db.Float)
    kickReturnTDs = db.Column(db.Float)
    twoPointConvertPasses = db.Column(db.Float)
    twoPointConvertRuns = db.Column(db.Float)
    twoPointConvertReceptions = db.Column(db.Float)
    fantasyPoints = db.Column(db.Float)
    fantasyPointsPPR = db.Column(db.Float)
    