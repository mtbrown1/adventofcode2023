import re

def isSymbol(char):
    isChar = char not in ['1','2','3','4','5','6','7','8','9','0','.']
    # print(char, isChar)
    return isChar

engineArray = []
with open('day03.input') as input:
    for line in input:
        engineArray.append([a for a in line if a != '\n'])

def checkSurrounding(partNumber):
    startRow = max(partNumber['row']-1, 0)
    endRow = min(partNumber['row']+1, len(engineArray)-1)
    startCol = max(partNumber['start']-1, 0)
    endCol = min(partNumber['end']+1, len(engineArray[0])-1)
    #print(partNumber['number'], (startRow, startCol), (endRow, endCol))
    numberSurrounds = ''
    isValid = False
    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol):
            numberSurrounds+=engineArray[row][col]
            if isSymbol(engineArray[row][col]):
                isValid = True
        numberSurrounds+='\n'
    #print(numberSurrounds, isValid)
    #print('--------------------')
    return isValid

partNumbers = []
for i in range(len(engineArray)):
    # print(engineArray[i])
    engineArrayLine = ''.join(engineArray[i])
    foundNumbers = re.finditer('\d+', engineArrayLine)
    # print(foundNumbers)
    partNumbers += [{'number': int(engineArrayLine[a.start():a.end()]), 'row': i, "start": a.start(), "end": a.end()} for a in foundNumbers]

print([pn['number'] for pn in partNumbers])
print(sum([pn['number'] for pn in partNumbers if checkSurrounding(pn)]))