import re
import itertools

def isSymbol(char):
    isChar = char not in ['1','2','3','4','5','6','7','8','9','0','.']
    # print(char, isChar)
    return isChar

engineArray = []
with open('day03.input') as input:
    for line in input:
        engineArray.append([a for a in line if a != '\n'])
# print(engineArray)

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

validParts = {pn['number']: True for pn in partNumbers if checkSurrounding(pn)}

def scanNumber(row, col):
    start=col
    end=col
    while engineArray[row][start].isdigit():
        start -= 1
        if start == -1:
            break
    start += 1
    while engineArray[row][end].isdigit():
        end += 1
        if end == len(engineArray[row]):
            break
    foundNumber = int("".join(engineArray[row][start:end]))
    #print(foundNumber)
    return foundNumber

def getGearPower(row, col):
    startRow = max(row-1,0)
    endRow = min(row+1,len(engineArray)-1)
    startCol = max(col-1,0)
    endCol = min(col+1,len(engineArray[row])-1)
    foundNumbers = set()
    for r in range(startRow, endRow+1):
        for c in range(startCol, endCol+1):
            if engineArray[r][c].isdigit():
                foundNumbers.add(scanNumber(r,c))
    #print(foundNumbers)
    if len(foundNumbers) == 2:
        asList = [a for a in foundNumbers]
        return asList[0]*asList[1]
    return 0

gearSum = 0
for i in range(len(engineArray)):
    for j in range(len(engineArray[i])):
        if engineArray[i][j] == '*':
            gearSum += getGearPower(i,j)
print(gearSum)