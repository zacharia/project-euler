#!/usr/bin/python

from math import *

size = 20

def make_grid(size):
    return [ [0 for i in range(size + 1)] for j in range(size + 1)]


def get_routes(grid):
    grid_size = len(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i > 0 and j > 0:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
            elif i == 0:
                grid[i][j] = 1
                #grid[i][j] += grid[i-1][j]
            elif j == 0:
                grid[i][j] = 1
                #grid[i][j] += grid[i][j-1]

    return grid[len(grid)-1][len(grid)-1]


def print_grid(grid):
    for i in grid:
        for j in i:
            print j,"\t",
        print "\n",

grid = make_grid(size)
print get_routes(grid)
print_grid(grid)
