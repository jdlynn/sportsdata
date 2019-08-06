from dotenv import load_dotenv
import os
import click
from flask import Flask
from flask.cli import with_appcontext
from app import create_app, db
from app.models import Stock, Projection
import requests

# from app.models import User, Post, Message, Notification, Task


app = create_app()

@app.cli.command()
def add_stock():
    response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players?key=eaf6aafbc0734ec7bc6e91b70072cd58')
    players = response.json()
    for player in players:
        myplayer = Stock( id=player['PlayerID'],
                    name=player['Name'], 
                    team=player['Team'], 
                    position=player['Position'],
                    age=player['Age'], 
                    experience=player['Experience'], 
                    jersey=player['Number'], 
                    photoURL=player['PhotoUrl'],
                    initialVal=5
                ) 
  
        db.session.add(myplayer)
        db.session.commit()

@app.cli.command()
def add_projection():
    response = requests.get('https://api.sportsdata.io/v3/nfl/projections/json/PlayerSeasonProjectionStats/2019?key=eaf6aafbc0734ec7bc6e91b70072cd58')
    projections = response.json()
    for projection in projections:
        myprojection = Projection( stockID=projection['PlayerID'],
                    passingYards=projection['PassingYards'], 
                    passingTDs = projection['PassingTouchdowns'],
                    passingInterceptions=projection['PassingInterceptions'], 
                    rushingAttempts=projection['RushingAttempts'],
                    rushingYards=projection['RushingYards'], 
                    rushingTouchdowns=projection['RushingTouchdowns'], 
                    receptions=projection['Receptions'], 
                    receivingYards=projection['ReceivingYards'],
                    receivingTDs=projection['ReceivingTouchdowns'],
                    fumblesLost=projection['FumblesLost'], 
                    puntReturnTDs=projection['PuntReturnTouchdowns'], 
                    kickReturnTDs=projection['KickReturnTouchdowns'], 
                    twoPointConvertPasses=projection['TwoPointConversionPasses'],
                    twoPointConvertRuns=projection['TwoPointConversionRuns'], 
                    twoPointConvertReceptions=projection['TwoPointConversionReceptions'], 
                    fantasyPoints=projection['FantasyPoints'], 
                    fantasyPointsPPR=projection['FantasyPointsPPR']
                ) 
  
        db.session.add(myprojection)
        db.session.commit()

@app.cli.command()
def add_initialValue():
    from sqlalchemy.orm import joinedload
    query = Stock
   
    for projection in projections:
        myprojection = Projection( stockID=projection['PlayerID'],
                    passingYards=projection['PassingYards'], 
                    passingTDs = projection['PassingTouchdowns'],
                    passingInterceptions=projection['PassingInterceptions'], 
                    rushingAttempts=projection['RushingAttempts'],
                    rushingYards=projection['RushingYards'], 
                    rushingTouchdowns=projection['RushingTouchdowns'], 
                    receptions=projection['Receptions'], 
                    receivingYards=projection['ReceivingYards'],
                    receivingTDs=projection['ReceivingTouchdowns'],
                    fumblesLost=projection['FumblesLost'], 
                    puntReturnTDs=projection['PuntReturnTouchdowns'], 
                    kickReturnTDs=projection['KickReturnTouchdowns'], 
                    twoPointConvertPasses=projection['TwoPointConversionPasses'],
                    twoPointConvertRuns=projection['TwoPointConversionRuns'], 
                    twoPointConvertReceptions=projection['TwoPointConversionReceptions'], 
                    fantasyPoints=projection['FantasyPoints'], 
                    fantasyPointsPPR=projection['FantasyPointsPPR']
                ) 
  
        db.session.add(myprojection)
        db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Stock': Stock, 'Projection': Projection}


