maxRed = 12
maxGreen = 13
maxBlue = 14

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

gamesSum = 0
with open("day02.input") as input:
    for game_line in input:
        game = parseGame(game_line)
        isPossible = True
        for round in game['rounds']:
            if round['red'] > maxRed or round['blue'] > maxBlue or round['green'] > maxGreen:
                isPossible = False
                break
        if isPossible: 
            gamesSum += game['number']
print(gamesSum)