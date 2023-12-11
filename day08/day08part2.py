import math

def steps_to_solution(startNode, directions, nodes):
    steps = 0
    iterated = []
    node = startNode[:]
    cd = 0
    while True:
        # print(node)
        if node[-1] == "Z":
            return steps
            #return (node, steps)
        node = nodes[node][directions[cd]]
        steps += 1
        cd += 1
        if cd == len(directions):
            cd = 0

with open("day08.input") as input:
    (directions, nodestext) = input.read().split('\n\n')

# print(directions)
nodestext = nodestext.split('\n')
nodes = {}
startingNodes = []
for node in nodestext:
    (k, v) = node.split(' = (')
    if k[-1] == "A":
        startingNodes.append(k)
    vals = v.split()
    nodes[k] = {'L': vals[0][:-1], 'R': vals[1][:-1]}

print(startingNodes)
multiples = [steps_to_solution(sn, directions, nodes) for sn in startingNodes]
print(multiples)
print(math.lcm(*multiples))