from dotenv import load_dotenv
import os
import click
from flask import Flask
from flask.cli import with_appcontext
from app import create_app, db
from app.models import Stock
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
                    initialVal=5) 
  
        db.session.add(myplayer)
        db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Stock': Stock}


