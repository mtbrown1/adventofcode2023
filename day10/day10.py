import math

(up,down,left,right) = ((-1,0),(1,0),(0,-1),(0,1))

def find_start(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "S":
                return (row,col)

def solve(field):
    start = find_start(field)
    for dir in [up,down,left,right]:
        # print("--------------------------------")
        loop = find_loop(start, field)
        # print(loop)
        if len(loop) > 0:
            return math.ceil(len(loop)/2)

def get_at(field, coords):
    return field[coords[0]][coords[1]]

def out_of_bounds(field, coords):
    return coords[0] < 0 or coords[0] >= len(field) or coords[1] < 0 or coords[1] >= len(field[0])

def next_direction(value, source):
    # print("Finding next direction:", value, source)
    if value == "|" and source in [down,up]:
        return source
    elif value == "-" and source in [left,right]:
        return source
    elif value == "L" and source in [down,left]:
        return up if source == left else right
    elif value == "J" and source in [down,right]:
        return up if source == right else left
    elif value == "7" and source in [up,right]:
        return down if source == right else left
    elif value == "F" and source in [up,left]:
        return down if source == left else right
    else:
        return None

def find_loop_recursive(path, direction, destination, field):
    # print("path so far:", path)
    nextspace = tuple(map(lambda i,j:i+j, path[-1], direction))
    if out_of_bounds(field, nextspace):
        # print("Hit an edge")
        return []
    value = get_at(field,nextspace)
    # print("Check next:", nextspace)
    if nextspace == destination:
        # print("Found the loop!")
        return path
    next_dir = next_direction(value,direction)
    if next_dir is None:
        # print("invalid pipe")
        return []
    path.append(nextspace)
    return find_loop(path, next_dir, destination, field)
    
def find_loop(start, field):
    path = [start]
    direction = right
    while True:
        nextspace = tuple(map(lambda i,j:i+j, path[-1], direction))
        if nextspace == start:
            # print("Found the loop!")
            return path
        if out_of_bounds(field, nextspace):
            # print("Hit an edge")
            return []
        value = get_at(field,nextspace)
        next_dir = next_direction(value,direction)
        if next_dir is None:
            # print("invalid pipe")
            return []
        path.append(nextspace)
        direction = next_dir


with open("day10.input") as input:
    field = [line for line in input.readlines()]

print(solve(field))