#!/usr/bin/python3
"""Blaire pascal's number immplemented"""


def pascal_triangle(n):
    """pascal_triangle implemented using python"""
    new_list = []
    if n <= 0:
        return new_list
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or j == 0:
                row.append(1)
            elif i > j:
                row.append(new_list[i-1][j-1] + new_list[i-1][j])
        new_list.append(row)
    return new_list
