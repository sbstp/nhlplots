from attr import attrs, attrib
import arrow
import requests


@attrs(slots=True)
class Game:
    id = attrib()
    goals = attrib(cmp=False)
    assists = attrib(cmp=False)
    date = attrib(cmp=False)


def get_player_gamelogs(player_id):
    resp = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=gameLog".format(player_id))
    data = resp.json()
    games = []
    for split in data['stats'][0]['splits']:
        game = Game(
            id=split['game']['gamePk'],
            goals=split['stat']['goals'],
            assists=split['stat']['assists'],
            date=arrow.get(split['date']),
        )
        games.append(game)
    return games
