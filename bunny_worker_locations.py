"""
Keeping track of Commander Lambda’s many bunny prisoners is starting to get tricky. You’ve been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda’s space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

| 7

| 4 8

| 2 5 9

| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

Write a function solution(x, y) which returns the prisoner ID of the bunny at the location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your solution as a string representation of the number.
"""

def bunny(x, y):
    # each column is a "cumulative sum sequence"
    # (n/2)*(n+1) to get nth sum
    # example x3, y2 -> 9
    # turns into x+(y-1) - (y-1)
    # turns into 4th - 1 -> 10 -1 = 9
    # example x5 y10 -> 96
    # turns to 14th - 9 = 105 - 9 = 96

    y = y - 1  # zero indexing
    return str(((x + y)/2)*((x + y)+1) - y)
