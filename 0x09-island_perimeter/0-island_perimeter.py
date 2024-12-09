#!/usr/bin/python3
"""calculates the perimeter of an island that's surronded by lakes and
also has lakes inside of it too."""


def island_perimeter(grid):
    """calculates the gird and returns the perimeter of the island."""
    peri = 0
    if grid is None:
        return None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if type(grid[row][col]) is not int:
                raise TypeError("invalid type of data.")
                return None
            if grid[row][col] < 0:
                raise ValueError("invalid value for the grid.")
                return
            if grid[row][col] == 0:
                continue
            else:
                peri += 1
    peri += 1
    return peri * 2
