import requests

response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players/WAS?key=eaf6aafbc0734ec7bc6e91b70072cd58')
players = response.json()
print('--Washington---')
for player in players:
    print(player['PlayerID'], '|', player['FirstName'],  player['LastName'], '|', player['FantasyPosition'])