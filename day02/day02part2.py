def parseGame(game_line):
    splitName = game_line.split(":")
    game = {
        'number': int(splitName[0][5:]),
        'rounds': []
    }
    for round in splitName[1].split(";"):
        parsedRound = {'blue': 0, 'green': 0, 'red': 0}
        for value in round.split(","):
            color = value.strip().split(" ")
            parsedRound[color[1]] = int(color[0])
        game['rounds'].append(parsedRound)
    return game

gamePowerSum = 0
with open("day02.input") as input:
    for game_line in input:
        game = parseGame(game_line)
        minPossible = game['rounds'][0]
        for round in game['rounds'][1:]:
            if round['red'] > minPossible['red']:
                minPossible['red'] = round['red']
            if round['blue'] > minPossible['blue']:
                minPossible['blue'] = round['blue']
            if round['green'] > minPossible['green']:
                minPossible['green'] = round['green']
        gamePowerSum += minPossible['red'] * minPossible['blue'] * minPossible['green']
print(gamePowerSum)