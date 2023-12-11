points = 0
with open("day04.input") as input:
    for line in input:
        splitName = line.split(": ")
        splitNumbers = splitName[1].split("|")
        winningNumbers = [int(i) for i in splitNumbers[0].strip().split()]
        selectedNumbers = [int(i) for i in splitNumbers[1].strip().split()]
        #print(winningNumbers, selectedNumbers)
        matches = 0
        for number in selectedNumbers:
            if number in winningNumbers:
                matches += 1
        points += pow(2,matches-1) if matches > 0 else 0
print(points)