TEST_INPUT = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

def main():
    
    # dots, fold_instructions = (x.splitlines() for x in TEST_INPUT.split('\n\n'))
    # dots = [[int(i) for i in d.split(',')] for d in dots]

    with open('inputs/d13.txt') as f:
        dots, fold_instructions = (x.splitlines() for x in f.read().split('\n\n'))
    dots = [[int(i) for i in d.split(',')] for d in dots]

    fold_instructions = [i.replace('fold along ', '').split('=') for i in fold_instructions]
    
    matrix = parse_dot_coords(dots)

    #pprint(matrix)

    for instruction in fold_instructions:

        if instruction[0] == 'y':
            f1, f2 = _split_on_y(matrix, int(instruction[1]))
            matrix = fold_y(f1, f2)
        elif instruction[0] == 'x':
            f1, f2 = _split_on_x(matrix, int(instruction[1]))
            matrix = fold_x(f1, f2)


    pprint(matrix)
    
    num_visible = count_num_visible(matrix)
    
    print(num_visible)


def parse_dot_coords(dots):
    
    max_x = max(l[0] for l in dots)
    max_y = max(l[1] for l in dots)

    matrix = [['' for _ in range(max_x+1)] for _ in range(max_y+1)]
    
    for dot in dots:
        matrix[dot[1]][dot[0]] = '#'

    return matrix

def fold_y(m1, m2):

    merged = []

    for i, row in enumerate(reversed(m1)):
        try:
            opposite_row = m2[i]
            merged_row = merge_rows(row, opposite_row)
        except IndexError:
            merged_row = row
        merged.insert(0, merged_row)

    return merged

def fold_x(m1, m2):

    merged = []

    for i, row in enumerate(m1):
        other_row = list(reversed(m2[i]))
        merged.append(merge_rows(row, other_row))
    
    return merged



def _split_on_x(matrix, x):

    left = [row[:x] for row in matrix]
    right = [row[x+1:] for row in matrix]

    return left, right

def _split_on_y(matrix, y):

    return matrix[:y], matrix[y+1:]



def merge_rows(r1, r2):

    merged_row = []

    for i, item in enumerate(r1):
        to_put = '#' if (item == '#' or r2[i] == '#') else ''
        merged_row.append(to_put)
    
    return merged_row


def count_num_visible(matrix):

    num_visible = 0

    for row in matrix:
        for item in row:
            if item == '#':
                num_visible += 1

    return num_visible



def pprint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            to_print = '.' if matrix[i][j] == '' else matrix[i][j]
            print(to_print, end=' ')
        print()
    





if __name__ == '__main__':
    main()