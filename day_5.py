from copy import deepcopy

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
        coord_from = row[0]
        coord_to = row[1]

        x_from = coord_from[0] #    1   
        x_to = coord_to[0] #        3   
        y_from = coord_from[1] #    1   
        y_to = coord_to[1] #        3   

        x_dir = 1 if x_from <= x_to else -1 #1
        y_dir = 1 if y_from <= y_to else -1 #1

        if (x_from == x_to) or (y_from == y_to):
            for x in range(x_from, x_to+x_dir, x_dir):
                if x_from - x_to != 0:
                    grid[y_from][x] += 1
            
            for y in range(y_from, y_to+y_dir, y_dir):
                if y_from - y_to != 0:
                    grid[y][x_from] += 1

            
        

        
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