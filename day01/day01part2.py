import re

numberwords = {
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9
}
numberwords.update({str(i): i for i in range(10)})

def findNumbers(input_string):
    foundIndexes = []
    for numword in numberwords.keys():
        foundIndexes += re.finditer(numword, input_string)
    foundIndexes.sort(key=lambda x: x.start())
    return [input_string[i.start():i.end()] for i in foundIndexes]

# strline = "2shgathreeajsf456d;threeasldfh"
# print(findNumbers(strline))

calibration = 0
with open('day01.input') as input:
    for line in input:
        digits = findNumbers(line)
        toadd = (numberwords[digits[0]]*10)+numberwords[digits[-1]]
        calibration += toadd
print(calibration)
