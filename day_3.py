from collections import Counter

TEST_INPUT = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

def main():
    
    test_input = TEST_INPUT.splitlines()
    with open('inputs/d3.txt') as f:
        real_input = f.read().splitlines()

    # Part 1

    test_bit_occurrences = count_bit_occurrences(test_input)
    test_power_consumption = get_power_consumption(test_bit_occurrences)
    
    print(f'Part 1 test solution: {test_power_consumption}')
    
    bit_occurrences = count_bit_occurrences(real_input)
    power_consumption = get_power_consumption(bit_occurrences)

    print(f'Part 1 real solution: {power_consumption}')
    
    # Part 2
    test_oxygen_generator_rating = get_oxygen_generator_rating(test_input)
    test_co2_scrubber_rating = get_co2_scrubber_rating(test_input)
    print(f'Part 2 test solution: {test_oxygen_generator_rating * test_co2_scrubber_rating}')

    real_oxygen_generator_rating = get_oxygen_generator_rating(real_input)
    real_co2_scrubber_rating = get_co2_scrubber_rating(real_input)
    print(f'Part 2 real solution: {real_oxygen_generator_rating * real_co2_scrubber_rating}')


def count_bit_occurrences(lst: list[str]) -> list[list]:
    """Count the number of times a bit occurs in a given position
    It will return a list where each element represents the count of 0s and 1s 
    in the full input respectively
    Example:
    0011
    1100
    1010
    will return [[1,2], [2,1], [1,2], [2,1]]

    Parameters
    ----------
    lst : list
        The list to read in
    Returns
    -------
    count_bits : list
        The count of 0s and 1s in each position of the input
    """

    count_bits = [[0, 0] for _ in range(len(lst[0]))]
    
    for num in lst:
        for i, bit in enumerate(num):
            bit_as_int = int(bit)
            count_bits[i][bit_as_int] += 1
    
    return count_bits


def get_power_consumption(bit_occurrences: list) -> int:
    """Take in the number of bit occurrences and calculate the gamma and epsilon rate as:
    Gamma: 0 if the most common bit is 0 in each position else 1
    Epsilon: 1 if the most common bit is 1 in each position else 0
    
    Parameters
    ----------
    bit_occurrences : list
        As returned by count_bit_occurrences()
    
    Returns
    -------
    power_consumption : int
        gamma_rate multiplied by epsilon_rate
    """

    gamma_rate = ('').join('0' if i[0] > i[1] else '1' for i in bit_occurrences)
    epsilon_rate = ('').join('1' if i[0] > i[1] else '0' for i in bit_occurrences)

    return _bin_to_dec(gamma_rate) * _bin_to_dec(epsilon_rate)


def get_oxygen_generator_rating(lst: list) -> int:
    """Go through list, and at each step, count the number of 0s and 1s vertically for each position.
    If there are more 1s, keep only elements that have an 1 in that position,
    and othervise keep only elements that have a 0 in that position
    If there is an equal number, keep ones that have a 1
    
    Parameters
    ----------
    lst : list
        The list to go through
    
    Returns
    -------
    oxygen_generator_rating : int
        The last number left after the reduction, converted to decimal
    """

    to_reduce = lst[:]

    for pos in range(len(lst[0])):
        cnt = Counter(x[pos] for x in to_reduce)
        if cnt['1'] >= cnt['0']:
            to_reduce = _reduce_list(to_reduce, '1', pos)
        else: # < 
            to_reduce = _reduce_list(to_reduce, '0', pos)
        
        if len(to_reduce) == 1:
            return _bin_to_dec(to_reduce[0])


def get_co2_scrubber_rating(lst: list) -> int:
    """Go through list, and at each step, count the number of 0s and 1s vertically for each position.
    If there are more 0s, keep only elements that have an 1 in that position,
    and othervise keep only elements that have a 1 in that position
    If there is an equal number, keep ones that have a 0
    
    Parameters
    ----------
    lst : list
        The list to go through
    
    Returns
    -------
    co2_scrubber_rating : int
        The last number left after the reduction, converted to decimal
    """

    to_reduce = lst[:]

    for pos in range(len(lst[0])):
        cnt = Counter(x[pos] for x in to_reduce)
        if cnt['0'] > cnt['1']:
            to_reduce = _reduce_list(to_reduce, '1', pos)
        else: # <=
            to_reduce = _reduce_list(to_reduce, '0', pos)
        
        if len(to_reduce) == 1:
            return _bin_to_dec(to_reduce[0])


def _reduce_list(lst: list[str], keep: str, idx: int) -> list[str]:
    """Helper function to reduce a list of strings and keep only
    strings where the character at a given idx is the same as the keep value
    
    Parameters
    ----------
    lst : list[str]
        A list of strings to reduce
    keep : str
        Element will be kept if this value is the same in it at the given index
    idx : int
        Element will be kept if the 'keep' value is the same in it at this index
    """

    return [element for element in lst if element[idx] == keep]


def _bin_to_dec(bin: str) -> int:
    """Helper function to convert a binary in string representation to an integer
    
    Parameters
    ----------
    bin : str
        The binary number as string
    
    Returns
    -------
    int
        The integer value of that binary number"""
    return int(bin, 2)


if __name__ == '__main__':
    main()