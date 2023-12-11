calibration = 0
with open('day01.input') as input:
    for line in input:
        digits = [int(l) for l in line if l.isdigit()]
        calibration += (digits[0]*10)+digits[-1]
print(calibration)