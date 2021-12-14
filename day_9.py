from copy import deepcopy
from pprint import pprint


TEST_INPUT = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

def main():

    test_input = parse_input(TEST_INPUT)

    with open('inputs/d9.txt') as f:
        real_input = parse_input(f.read())

    print(get_low_points(test_input))
    


def get_low_points(inp: list[list]) -> int:

    flood_filled = deepcopy(inp)

    low_points = 0

    for i, row in enumerate(inp):
        for j, num in enumerate(row):

            num_above = _get_num_from_list(i-1, j, inp)
            num_below = _get_num_from_list(i+1, j, inp)
            num_left = _get_num_from_list(i, j-1, inp)
            num_right = _get_num_from_list(i, j+1, inp)

            if num_above > num and num_below > num and num_left > num and num_right > num:
                print(num_above, num_below, num_left, num_right, ' --- ', num, i, j)
                low_points += 1 + num
                #print(num, i, j)
                flood_filled = flood_fill(flood_filled, i, j, num)
    
                pprint(flood_filled)
    
    return low_points


def flood_fill(matrix: list[list], i: int, j: int, prev_num) -> list[list]:

    num = matrix[i][j]
    

    if num == prev_num:
        matrix[i][j] = 10

        if i > 0:
            flood_fill(matrix, i-1, j, prev_num + 1)
        if i < len(_get_value(matrix, j)) - 1:
            print(i, len(_get_value(matrix, j)))
            flood_fill(matrix, i + 1, j, prev_num + 1)
        if j > 0:
            flood_fill(matrix, i, j-1, prev_num + 1)
        if j < len(matrix) - 1:
            flood_fill(matrix, i, j + 1, prev_num + 1)

    
    return matrix
    

def _get_value(a, idx):
    try:
        return a[idx]
    except IndexError:
        if isinstance(a, list):
            return []
        else:
            return 0

    
def fill_basin_from_point(i: int, j: int, inp: list[list]) -> int:

    height = inp[i][j]
    basin_size = 1

    for next_height in range(height, 9):
        # 9 should be excluded

        num_above = _get_num_from_list(i-1, j, inp)
        num_below = _get_num_from_list(i+1, j, inp)
        num_left = _get_num_from_list(i, j-1, inp)
        num_right = _get_num_from_list(i, j+1, inp)

        if num_above == next_height:
            basin_size += 1
        if num_below == next_height:
            basin_size += 1
        if num_left == next_height:
            basin_size += 1
        if num_right == next_height:
            basin_size += 1



    while True:
        num_above = _get_num_from_list(i-1, j, inp)
        num_below = _get_num_from_list(i+1, j, inp)
        num_left = _get_num_from_list(i, j-1, inp)
        num_right = _get_num_from_list(i, j+1, inp)


def _get_num_from_list(i: int, j: int, inp: list[list]) -> int:
    if i < 0 or j < 0:
        return 11
    try:
        return inp[i][j]
    except IndexError:
        return 11
    



def parse_input(inp: str) -> list[list]:
    return [list(map(int, line)) for line in inp.splitlines()]


if __name__ == '__main__':
    main()