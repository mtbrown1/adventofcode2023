repeats = {}
lineIndex = 0
with open("day04.input") as input:
    for line in input:
        iterations = 1 + (repeats[lineIndex] if lineIndex in repeats else 0)
        # print(lineIndex, repeats)
        # print("iterations:", iterations)
        
        splitName = line.split(": ")
        splitNumbers = splitName[1].split("|")
        winningNumbers = [int(i) for i in splitNumbers[0].strip().split()]
        selectedNumbers = [int(i) for i in splitNumbers[1].strip().split()]
        # print(winningNumbers, selectedNumbers)
        matches = 0
        for number in selectedNumbers:
            if number in winningNumbers:
                matches += 1
        # print("matches: ", matches)
        for i in range(matches):
            extraCard = lineIndex + i + 1
            if extraCard in repeats:
                repeats[extraCard] += iterations
            else:
                repeats[extraCard] = iterations
        lineIndex += 1
print(sum(repeats.values())+lineIndex)