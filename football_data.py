from secret import my_token
from dates import *
import requests, json

url = 'http://api.football-data.org/'
matches = 'v4/matches?competitions=CL,BL1,PD,FL1,EC,SA,PL'
yesterday_matches = f'v4/matches?competitions=CL,BL1,PD,FL1,EC,SA,PL&dateFrom={dateFrom()}&dateTo={dateTo()}'
tables = {'pl': 'v4/competitions/PL/standings', 'pd': 'v4/competitions/PD/standings', 'bl': 'v4/competitions/BL1/standings', 'sa': 'v4/competitions/SA/standings', 'fl': 'v4/competitions/FL1/standings'}
header = {'X-Auth-Token': my_token}

def get_all_matches():
    response = requests.get(url + matches, headers=header).content
    json_object = json.loads(response)
    result = ''
    for item in json_object["matches"]:
        time = f'{int(item["utcDate"][11:13]) + 3}:{item["utcDate"][14:16]}'
        result += f'{item["homeTeam"]["shortName"]} - {item["awayTeam"]["shortName"]} | {time}\n'
    if result == '':
        return 'Матчей нет'
    else:
        return result[0:-1]

def get_results():
    response = requests.get(url + yesterday_matches, headers=header).content
    json_object = json.loads(response)
    result = ''
    for item in json_object["matches"]:
        scores = f'{item["score"]["fullTime"]["home"]}:{item["score"]["fullTime"]["away"]}'
        result = f'{item["homeTeam"]["shortName"]} - {item["awayTeam"]["shortName"]} | {scores}\n'
    if result == '':
        return 'Матчей нет'
    else:
        return result[0:-1]

def get_table(code: str):
    site = f'{url}{tables[code]}'
    response = requests.get(site, headers=header).content
    json_object = json.loads(response)
    table = 'Team           | G  | P  | W  | D  | L  | S  | C  | №\n'
    table += '______________________________________________________\n'
    for item in json_object["standings"][0]["table"]:
        team = item["team"]["shortName"]
        if len(team) < 14:
            team += ' ' * (14 - len(team))
        games = str(item["playedGames"])
        if len(games) == 1:
            games += ' '
        pts = str(item["points"])
        if len(pts) == 1:
            pts += ' '
        won = str(item["won"])
        if len(won) == 1:
            won += ' '
        draw = str(item["draw"])
        if len(draw) == 1:
            draw += ' '
        lost = str(item["lost"])
        if len(lost) == 1:
            lost += ' '
        goalsFor = str(item["goalsFor"])
        if len(goalsFor) == 1:
            goalsFor += ' '
        goalsAgainst = str(item["goalsAgainst"])
        if len(goalsAgainst) == 1:
            goalsAgainst += ' '
        position = str(item["position"])
        if len(position) == 1:
            position += ' '
        line = f'{team} | {games} | {pts} | {won} | {draw} | {lost} | {goalsFor} | {goalsAgainst} | {position}\n'
        table += line
    return table


