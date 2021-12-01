TEST_INPUT = '''199
200
208
210
200
207
240
269
260
263'''

def main():

    # Set up inputs
    test_input = [int (x) for x in TEST_INPUT.splitlines()]
    with open('inputs/d1.txt') as f:
        real_input = [int(x) for x in f.read().splitlines()]


    # Part 1
    print('Test part 1:', count_num_increases(test_input))
    print('Real part 1:', count_num_increases(real_input))

    # Part 2
    print('Test part 2:', increases_in_sliding_window(test_input))
    print('Real part 2:', increases_in_sliding_window(real_input))


def count_num_increases(lst: list[int]) -> int:
    """Find the number of times a given integer in a list of integers
    is bigger than the previous one
    
    Parameters
    ----------
    lst : list[int]
        The list of integers to parse
    
    Returns
    -------
    int
        The result
    """
    return sum(lst[i] > lst[i - 1] for i in range(1, len(lst)))

def increases_in_sliding_window(lst: list) -> int:
    """With a sliding window of 3 integers, compare all windows in a list
    and return the number of times the sum of a given window is bigger than
    the sum of the previous window

    Parameters
    ----------
    lst : list[int]
        The list of integers to parse
    
    Returns
    -------
    num_increases : int
        Number of times the sum of the window is increased compared to the previous one
    """
    
    # First time through the previous sum is just the sum of the first 3 elements
    prev_sum = sum(lst[:3])
    num_increases = 0

    # Start from the fourth element
    for i in range(3, len(lst)):
        # Sum the numbers from i-2 to i
        new_sum = sum(lst[i-2:i+1])
        if new_sum > prev_sum:
            num_increases += 1
        prev_sum = new_sum

    return num_increases


if __name__ == '__main__':
    main()

