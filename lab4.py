from typing import List
import data
import math

# Write your functions for each part in the space below.

# Part 1
# This function takes in a list containing nested integer list(s)
# and returns a list containing the first element of each nested
# list from the input.
def first_element(list : list[list[int]]) -> list:
    return [x[0] for x in list]

# Part 2
# This function x_coordinates takes in one parameter of type list[Point]
# This function will return a list containing the x-coordinate
# of each point in the input list.

def x_coordinates(points : list[data.Point]) -> list[data.Point]:
    return [i.x for i in points]

# Part 3
# This function are_in_positive_quadrant takes a list of Points as input and returns
# another list that contains all the points from the input
# that are in the first quadrant.
def are_in_positive_quadrant(points : list[data.Point]) -> list[data.Point]:
    return [i for i in points if i.x > 0 and i.y > 0]

# Part 4
# This function distance takes two arguments of type Point and returns
# the Euclidian distance between them.
def distance(a : data.Point, b : data.Point) -> float:
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

# Part 5
# This function manhattan_distance takes two argument of type Point
# and returns the Manhattan distance between them.
def manhattan_distance(a : data.Point, b : data.Point) -> float:
    return abs(b.x - a.x) + abs(b.y - a.y)

# Part 6
# This function distance_all takes in type list[Point] and
# returns a list containing the distance from the origin
# for each Point in the list.
def distance_all(points : list[data.Point]) -> list[float]:
    return [manhattan_distance(i, data.Point(0,0)) for i in points]

