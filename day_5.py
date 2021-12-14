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
    grid = create_grid(test_input)
    grid = place_points(test_input, grid)
    #overlaps = get_num_places_with_overlaps(grid)
    #print(overlaps)

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
            grid = place_vertical()
        elif y_to == y_from:
            grid = place_horizontal()
        else:
            pass
            # place diagonal left-right up
            # place diagonal left-right down
            # place diagonal right-left up
            # place diagonal right-left down
        

 

        
    print_grid(grid)


def draw_line(mat, x0, y0, x1, y1, inplace=False):
    if not (0 <= x0 < mat.shape[0] and 0 <= x1 < mat.shape[0] and
            0 <= y0 < mat.shape[1] and 0 <= y1 < mat.shape[1]):
        return mat
    if not inplace:
        mat = mat.copy()
    if (x0, y0) == (x1, y1):
        mat[x0, y0] = 2
        return mat if not inplace else None
    # Swap axes if Y slope is smaller than X slope
    transpose = abs(x1 - x0) < abs(y1 - y0)
    if transpose:
        mat = mat.T
        x0, y0, x1, y1 = y0, x0, y1, x1
    # Swap line direction to go left-to-right if necessary
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    # Write line ends
    mat[x0, y0] += 1
    mat[x1, y1] += 1
    # Compute intermediate coordinates using line equation
    x = np.arange(x0 + 1, x1)
    y = np.round(((y1 - y0) / (x1 - x0)) * (x - x0) + y0).astype(x.dtype)
    # Write intermediate coordinates
    mat[x, y] += 1
    if not inplace:
        return mat if not transpose else mat.T

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


'''
1 1
2 2
3 3   

9 4     
8 4     
7 4     
6 4     
5 4     
3 4     
'''

            

    

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