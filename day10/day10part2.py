import math
from shapely.geometry import LineString, Point

(up,down,left,right) = ((-1,0),(1,0),(0,-1),(0,1))

def find_start(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "S":
                return (row,col)

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

def find_loop(start, field):
    path = [start]
    for direction in [up,down,left,right]:
        while True:
            nextspace = tuple(map(lambda i,j:i+j, path[-1], direction))
            if nextspace == start:
                # print("Found the loop!")
                return path
            if out_of_bounds(field, nextspace):
                # print("Hit an edge")
                break
            value = get_at(field,nextspace)
            next_dir = next_direction(value,direction)
            if next_dir is None:
                # print("invalid pipe")
                break
            path.append(nextspace)
            direction = next_dir

def loop_as_edges(loop):
    edges = []
    prev = (loop[0],loop[1])
    for point in loop[2:]:
        if (prev[0][0]-point[0]) == 0 or (prev[0][1]-point[1]) == 0:
            prev = (prev[0],point)
        else:
            edges.append(prev)
            prev = (prev[1],point)
    edges.append((edges[-1][1],loop[0]))
    return edges

def line_intersection(line1, line2):
    p1 = Point((line1[0][1],line1[0][0]))
    p2 = Point((line1[1][1],line1[1][0]))
    p3 = Point((line2[0][1],line2[0][0]))
    p4 = Point((line2[1][1],line2[1][0]))
    l1 = LineString((p1,p2))
    l2 = LineString((p3,p4))
    intersection = l1.intersection(l2)
    if intersection and type(intersection) == Point:
        return True
    return False

def solve_old(field):
    start = find_start(field)
    loop_points = find_loop(start, field)
    loop = loop_as_edges(loop_points)
    print(loop)
    contained = 0
    for row in range(len(field)):
        for col in range(len(field[row])):
            print("----------------------------------------")
            print("Checcking point", (col,row))
            if (row,col) not in loop_points:
                intersects = 0
                shortest = min(row,col)
                intersectLine = ((row-shortest,col-shortest),(row,col))
                for edgeline in loop:
                    if line_intersection(edgeline,intersectLine):
                        intersects += 1
                if intersects % 2 == 1:
                    print("Point ", (col,row), "is within the loop, intersecting", intersects, "edges")
                    contained += 1
    return contained

s_real_value = "-"
def solve(field):
    start = find_start(field)
    loop_points = find_loop(start, field)
    # loop = loop_as_edges(loop_points)
    # print(loop)
    field[start[0]] = field[start[0]].replace("S",s_real_value)
    print(field)
    contained = 0
    for row in range(len(field)):
        for col in range(len(field[row])):
            if (row,col) not in loop_points:
                cur = (row,col)
                intersects = 0
                while cur[0]>-1 and cur[1]>-1:
                    if cur in loop_points and get_at(field,cur) in ["|","-","J","F"]:
                        intersects += 1
                    cur = (cur[0]-1, cur[1]-1)
                if intersects % 2 == 1:
                    #print("Point ", (col,row), "is within the loop, intersecting", intersects, "edges")
                    contained += 1
    return(contained)

with open("day10.input") as input:
    field = [line.strip() for line in input.readlines()]

print(solve(field))