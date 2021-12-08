from math import floor, ceil

TEST_INPUT = '16,1,2,0,4,2,7,1,2,14'

def main():

    test_input = [int(x) for x in TEST_INPUT.split(',')]
    
    with open('inputs/d7.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    
    pt1_test_solution = calculate_best_position_pt1(test_input)
    pt1_real_solution = calculate_best_position_pt1(inp)

    print(f'Part 1 test solution: {pt1_test_solution}')
    print(f'Part 1 real solution: {pt1_real_solution}')

    pt2_test_solution = calculate_best_position_pt2(test_input)
    pt2_real_solution = calculate_best_position_pt2(inp)

    print(f'Part 2 test solution: {pt2_test_solution}')
    print(f'Part 2 real solution: {pt2_real_solution}')
    

def calculate_best_position_pt1(crabs: list[int]) -> int:

    sorted_crabs = sorted(crabs)
    mid_point = int(len(sorted_crabs) / 2)
    
    sum_fuel = 0

    for crab_pos in sorted_crabs:
        fuel_needed = abs(crab_pos - sorted_crabs[mid_point])
        #print(f'Move from {crab_pos} to {sorted_crabs[mid_point]}: {fuel_needed} fuel')
        sum_fuel += fuel_needed
        
    
    return sum_fuel

def calculate_best_position_pt2(crabs: list[int]) -> int:

    # since mean lies within 0.5 of the solution, we have 2 possibilities
    # (eg. for test _b works, but for real input _a works)
    best_position_a = floor(sum(crabs) / len(crabs)) # round down
    best_position_b = ceil(sum(crabs) / len(crabs)) # round up

    sum_fuel_a = 0
    sum_fuel_b = 0

    for crab_pos in crabs:
        fuel_needed_a = sum(range(1, abs(crab_pos - best_position_a) + 1))
        fuel_needed_b = sum(range(1, abs(crab_pos - best_position_b) + 1))
        #print(f'Move from {crab_pos} to {best_position}: {fuel_needed} fuel')
        sum_fuel_a += fuel_needed_a
        sum_fuel_b += fuel_needed_b

    return (sum_fuel_a, sum_fuel_b)


if __name__ == '__main__':
    main()