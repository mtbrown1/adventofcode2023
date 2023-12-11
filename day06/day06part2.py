'''
time of the race = t
speed = x
x is how long you hold the button
traveled = x(t-x)
record = r
find where x(t-x) > r 
solve for r = x(t-x)

so...
t = 7
r = 9
9 = x(7-x)
0 = -x^2 +7x -9
0 = (-x+a)(x-b)
'''

import math

def easy_quadratic(b,c):
    a = -1
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    return (x1,x2)

def modifeid_ceil(x):
    return math.ceil(x) if math.ceil(x) != x else int(x)+1

def modified_floor(x):
    return math.floor(x) if math.floor(x) != x else int(x)-1

def solve(time, record):
    intersects = easy_quadratic(time, record*-1)
    winning_range = [modifeid_ceil(y) for y in intersects]
    return 1 + modified_floor(intersects[1]) - modifeid_ceil(intersects[0])
a,b,c = (-1, 7, -9)
# y = ax^2 + bx + c

with open("day06.input") as input:
    lines = input.readlines()
    t = int(lines[0].split(":")[1].replace(" ", ""))
    r = int(lines[1].split(":")[1].replace(" ", ""))

print(solve(t,r))
