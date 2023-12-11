def solve(directions, nodes):
    steps = 0
    i = 0
    location = "AAA"
    while True:
        if location == "ZZZ":
            return steps
        location = nodes[location][directions[i]]
        steps += 1
        i = i+1 if i < len(directions)-1 else 0

with open("day08.input") as input:
    (directions, nodestext) = input.read().split('\n\n')

# print(directions)
nodestext = nodestext.split('\n')
nodes = {}
for node in nodestext:
    (k, v) = node.split(' = (')
    vals = v.split()
    nodes[k] = {'L': vals[0][:-1], 'R': vals[1][:-1]}
# print(nodes)
print(solve(directions, nodes))

