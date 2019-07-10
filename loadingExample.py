import requests

response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players?key=eaf6aafbc0734ec7bc6e91b70072cd58')
players = response.json()
print('--Washington---')
for player in players:
    print(player['PlayerID'], '|', player['Team'], '|', player['Name'], '|',
    player['Position'], '|', player['Age'], '|', player['Number'], '|', player['Experience'],
    '|', player['PhotoUrl'])