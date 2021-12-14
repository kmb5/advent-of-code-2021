from pprint import pprint
from copy import deepcopy

TEST_INPUT = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

TOTAL_NUM_FLASHES = 0
FLASHED_IN_STEP = 0

def main():
    
    with open('inputs/d11.txt') as f:
        real_input = parse_input(f.read())

    part_1(real_input)
    part_2(real_input)
    
    

def part_1(inp):

    inp = deepcopy(inp)

    for _ in range(100):
        simulate_step(inp)
    
    print(f'Part 1 solution: {TOTAL_NUM_FLASHES}')
    

def part_2(inp):

    inp = deepcopy(inp)

    global FLASHED_IN_STEP

    num_steps = 0

    while FLASHED_IN_STEP != 100:
        simulate_step(inp)
        num_steps += 1
    
    print(f'Part 2 solution: {num_steps}')



def simulate_step(inp: list[list]):

    global FLASHED_IN_STEP
    FLASHED_IN_STEP = 0

    for x in range(len(inp)):
        for y in range(len(inp[x])):
            inp[x][y] += 1
        
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            if inp[x][y] > 9:
                _flash(x, y, inp)
    
    #print(FLASHED_IN_STEP)
            


def _flash(row: int, col: int, lst: list[list]):

    # if lst[row][col] <= 9:
    #     return lst
    
    #print(f'flashed at {row, col}')
    lst[row][col] = 0
    global TOTAL_NUM_FLASHES, FLASHED_IN_STEP
    TOTAL_NUM_FLASHES += 1
    FLASHED_IN_STEP += 1
    #pprint(lst)
    #print()

    # horizontal
    if _get_element(row-1, col, lst) not in (-1, 0):
        lst[row-1][col] += 1
        if lst[row-1][col] > 9:
            _flash(row-1, col, lst)
    if _get_element(row+1, col, lst) not in (-1, 0):
        lst[row+1][col] += 1
        if lst[row+1][col] > 9:
            _flash(row+1, col, lst)

    # vertical
    if _get_element(row, col-1, lst) not in (-1, 0):
        lst[row][col-1] += 1
        if lst[row][col-1] > 9:
            _flash(row, col-1, lst)
    if _get_element(row, col+1, lst) not in (-1, 0):
        lst[row][col+1] += 1
        if lst[row][col+1] > 9:
            _flash(row, col+1, lst)
    
    # diagonal
    if _get_element(row-1, col-1, lst) not in (-1, 0):
        lst[row-1][col-1] += 1
        if lst[row-1][col-1] > 9:
            _flash(row-1, col-1, lst)
    if _get_element(row-1, col+1, lst) not in (-1, 0):
        lst[row-1][col+1] += 1
        if lst[row-1][col+1] > 9:
            _flash(row-1, col+1, lst)
    if _get_element(row+1, col-1, lst) not in (-1, 0):
        lst[row+1][col-1] += 1
        if lst[row+1][col-1] > 9:
            _flash(row+1, col-1, lst)
    if _get_element(row+1, col+1, lst) not in (-1, 0):
        lst[row+1][col+1] += 1
        if lst[row+1][col+1] > 9:
            _flash(row+1, col+1, lst)
    
        

def _get_element(row, col, lst):
    
    if row < 0 or col < 0:
        return -1
    try:
        return lst[row][col]
    except IndexError:
        return -1


def parse_input(inp: str) -> list[list]:

    return [[int(num) for num in row] for row in inp.splitlines()]



if __name__ == '__main__':
    main()
