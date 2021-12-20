from copy import deepcopy
import numpy as np

TEST_INPUT = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

from pprint import pprint

def main():
    
    test_input = parse_input(TEST_INPUT)
    
    with open('inputs/d5.txt') as f:
        real_input = parse_input(f.read())
    grid = create_grid(real_input)
    grid = place_points(real_input, grid)
    #print_grid(grid)
    overlaps = get_num_places_with_overlaps(grid)
    print(overlaps)

def get_num_places_with_overlaps(filled_grid: list[list]) -> int:
    num_places_with_overlaps = 0

    for row in filled_grid:
        for num in row:
            if num > 1:
                num_places_with_overlaps += 1
        
    return num_places_with_overlaps


def place_points(inp: list[list], grid: list[list]) -> list[list]:
    
    grid = deepcopy(grid)

    for row in inp:
        x_from, y_from = row[0]
        x_to, y_to = row[1]

        if x_to == x_from:
            #print('placing vertical', x_from, y_from, ' ', x_to, y_to)
            grid = place_vertical(x_to, y_from, y_to, grid)
            #print_grid(grid)
        elif y_to == y_from:
            #print('placing horizontal', x_from, y_from, ' ', x_to, y_to)
            grid = place_horizontal(y_to, x_from, x_to, grid)
            #print_grid(grid)
        elif x_from < x_to and y_from < y_to:
            # place diagonal left-right up
            grid = place_diagonal_left_down(x_from, y_from, x_to, y_to, grid)
        elif x_from < x_to and y_from > y_to:
            # place diagonal left-right down
            grid = place_diagonal_left_up(x_from, y_from, x_to, y_to, grid)
        elif x_from > x_to and y_from < y_to:
            # place diagonal right-left up
            grid = place_diagonal_right_down(x_from, y_from, x_to, y_to, grid)
        elif x_from > x_to and y_from > y_to:
            # place diagonal right-left down
            grid = place_diagonal_right_up(x_from, y_from, x_to, y_to, grid)
            
        
    return grid

def place_vertical(x, y_from, y_to, grid):

    start_y = y_from if y_from < y_to else y_to
    end_y = y_to if y_from < y_to else y_from

    for y in range(start_y, end_y+1):
        grid[y][x] += 1
    
    return grid

def place_horizontal(y, x_from, x_to, grid):

    start_x = x_from if x_from < x_to else x_to
    end_x = x_to if x_from < x_to else x_from

    #print(start_x, end_x)

    for x in range(start_x, end_x+1):
        grid[y][x] += 1
    
    return grid

def place_diagonal_left_down(x_from, y_from, x_to, y_to, grid):

    #print('diag left down', x_from, y_from, x_to, y_to)

    x = x_from
    y = y_from
    
    for _ in range(x_from, x_to+1):
        grid[y][x] += 1
        x += 1
        y += 1
    
    return grid

def place_diagonal_left_up(x_from, y_from, x_to, y_to, grid):

    x = x_from
    y = y_from
    
    for _ in range(x_from, x_to + 1):
        grid[y][x] += 1
        x += 1
        y -= 1
    
    return grid

def place_diagonal_right_up(x_from, y_from, x_to, y_to, grid):

    x = x_from
    y = y_from
    
    for _ in range(x_from, x_to - 1, -1):
        grid[y][x] += 1
        x -= 1
        y -= 1

    return grid

def place_diagonal_right_down(x_from, y_from, x_to, y_to, grid):
    
    x = x_from
    y = y_from
    
    for _ in range(x_from, x_to - 1, -1):
        grid[y][x] += 1
        x -= 1
        y += 1

    return grid

    



def print_grid(grid):

    ggrid = ''
    for row in grid:
        r = ''
        for n in row:
            if n == 0:
                r += '.' + ' '
            else:
                r += str(n) + ' '
        ggrid += r + '\n'
    
    print(ggrid)
    

def create_grid(inp: list[list]) -> list[list]:
    max_x = 0
    max_y = 0
    for row in inp:
        x = max(r[0] for r in row)
        y = max(r[1] for r in row)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    #return np.zeros((max_x, max_y))
    return [[0 for _ in range(max_y+2)] for _ in range(max_x+2)]
        


def parse_input(inp: str) -> list:
    ret = []
    for line in inp.splitlines():
        s = line.split(' -> ')
        row = []
        for n in s:
            sn = [int(a) for a in n.split(',')]
            row.append(sn)
        ret.append(row)
    return ret
    #return [line.split(' -> ') for line in inp.splitlines()]


if __name__ == '__main__':
    main()