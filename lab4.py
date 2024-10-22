from typing import List
import data
import math

# Write your functions for each part in the space below.

# Part 1
# Returns a list of the first element of each nested list from the input
# INPUT: list nested with list(s) of type Int
# OUTPUT: list of integers
def first_element(list : list[list[int]]) -> list:
    return [x[0] for x in list]

# Part 2
# Gets the x-coordinates of each point in the list
# INPUT: list of Points
# OUTPUT: list containing the x-coordinates of each point in the argument
def x_coordinates(points : list[data.Point]) -> list[float]:
    return [i.x for i in points]

# Part 3
# Retrieves all the points in a list that have positive x and y values
# INPUT: list of Points
# OUTPUT: list of Points that have positive x and y values
def are_in_positive_quadrant(points : list[data.Point]) -> list[data.Point]:
    return [i for i in points if i.x > 0 and i.y > 0]

# Part 4
# Calculates the Euclidian distance between two points
# INPUT: two arguments of type Point
# OUTPUT: float of the Euclidian distance
def distance(a : data.Point, b : data.Point) -> float:
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

# Part 5
# Calculates the Manhattan distance between two points
# INPUT: two arguments of type Point
# OUTPUT: float of the Manhattan distance
def manhattan_distance(a : data.Point, b : data.Point) -> float:
    return abs(b.x - a.x) + abs(b.y - a.y)

# Part 6
# Calculates the distance from the origin for each point in the list
# INPUT: list of Points
# OUTPUT: list of floats of the distance between each point in the list and the origin
def distance_all(points : list[data.Point]) -> list[float]:
    return [manhattan_distance(i, data.Point(0,0)) for i in points]

