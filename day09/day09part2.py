def get_prev(numbers):
    if all(n==0 for n in numbers):
        return 0
    else:
        return numbers[0] - (get_prev([numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]))

sequences = []
with open("day09.input") as input:
    for line in input:
        sequences.append([int(i) for i in line.split()])

newnumbers = 0
for sequence in sequences:
    newnumbers += get_prev(sequence)
print(newnumbers)