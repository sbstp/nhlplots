from . import api
import matplotlib.pyplot as plt
import sys
import re

url = sys.argv[1]
# https://www.nhl.com/player/nikita-kucherov-8476453
m = re.search(r"/player/.+\-(\d+)", url)
id = int(m.group(1))

games = api.get_player_gamelogs(id)
games.sort(key=lambda g: g.date)


goals = 0
assists = 0
points = 0

x = list(range(0, len(games) + 1, 5))

d_goals = []
d_assists = []
d_points = []

for game in games:
    goals += game.goals
    assists += game.assists
    points += game.goals + game.assists
    d_goals.append(goals)
    d_assists.append(assists)
    d_points.append(points)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Game #')

plt.plot(d_goals, label="Goals")
plt.plot(d_assists, label="Assists")
plt.plot(d_points, label="Points")
plt.xticks(x, [a + 1 for a in x])
plt.legend()

plt.tight_layout()
plt.savefig("foo.png", bbox_inches='tight', dpi=200)
# plt.show()
