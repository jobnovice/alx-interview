#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    grid2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]
   
    print(island_perimeter(grid2))


    grid3 = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0]
            ]
    
    print(f'perimeter for grid3: {island_perimeter(grid3)}')
    grid4 = [[0, 1, 0, 0, 0, 1],
             [1, 1, 0, 0, 0, 1],
             [1, 1, 0, 1, 1, 1],
             [0, 1, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0]
             ]
    print(f'perimeter for grid4: {island_perimeter(grid4)}')

    grid5 = [[0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [1, 1, 1, 0, 0, 0],
             [0, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 1, 1]
             ]


    print(f'perimeter for grid5: {island_perimeter(grid5)}')


