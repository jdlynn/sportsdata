from flask import current_app, url_for
from app import db
import datetime
from sqlalchemy.ext.hybrid import hybrid_property

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
    updateDate = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    createDate = db.Column(db.DateTime, default=datetime.datetime.now())
    projections = db.relationship('Projection', backref=db.backref('stocks', lazy=True), uselist=False)

    def __repr__(self):
        return 'Stock {}'.format(self.name)

    @hybrid_property
    def projval(self):
        if not self.projections:
            return 5
        myProj = self.projections
        if self.position == "TE":
            points = (myProj.passingYards * .04 + 
                      myProj.passingTDs * 4 + 
                      myProj.passingInterceptions * -2 + 
                      myProj.rushingAttempts * .25 + 
                      myProj.rushingYards * .1 + 
                      myProj.rushingTouchdowns * 6 + 
                      myProj.receptions * 1.5 + 
                      myProj.receivingYards * .125 + 
                      myProj.receivingTDs * 6 + 
                      myProj.fumblesLost * -2) / 8
        else:
            points = (
                      myProj.passingYards * .04 + 
                      myProj.passingTDs * 4 + 
                      myProj.passingInterceptions * -2 + 
                      myProj.rushingAttempts * .25 + 
                      myProj.rushingYards * .1 + 
                      myProj.rushingTouchdowns * 6 + 
                      myProj.receptions * 1 + 
                      myProj.receivingYards * .1 + 
                      myProj.receivingTDs * 6 + 
                      myProj.fumblesLost * -2) / 8
        if points < 5:
            points = 5
        return points

class Projection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stockID = db.Column(db.Integer, db.ForeignKey('stock.id'))
    passingYards = db.Column(db.Float)
    passingTDs  =db.Column(db.Float)
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
    updateDate = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    createDate = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return 'Projection {}'.format(self.stockID)
    