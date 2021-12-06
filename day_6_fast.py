def main():

    with open('inputs/d6.txt') as f:
        fishes = parse_input(f.read())
    
    part_1 = run_for_n_days(80, fishes)
    part_2 = run_for_n_days(256, fishes)

    print(part_1)
    print(part_2)

def run_for_n_days(n: int, fishes: list[int]) -> int:
    """Run the simulation for n days and return the sum of fishes at
    the end of the simulation.
    
    Parameters
    ----------
    n : int
        The number of days to simulate
    fishes : list[int]
        The starting list of fishes to do the simulation with
    """

    fishes = fishes.copy()

    for _ in range(n):

        for i, num_fishes in enumerate(fishes):

            if num_fishes == 0:
                # if there are 0 fishes at this index, we can safely skip
                continue

            if i == 0:
                # skip 0th element because that signals all fishes
                # that will give birth at the end of the day
                continue

            # move all fishes to the left
            fishes[i-1] = num_fishes
            fishes[i] = 0
            
        # at the end of the turn, give birth
        # and reset the amount of fishes giving birth
        if fishes[0] != 0:
            fishes[7] += fishes[0]
            fishes[9] += fishes[0]
            fishes[0] = 0
    
    return sum(fishes)
        
            
def parse_input(inp: str) -> list[int]:
    """Parses the string of fish 'timings' into a list
    where each index(+1) corresponds to the fish timing
    and each element is the number of fishes currently at that timing
    The list is fixed len() = 10 because no fish has a timing > 8
    * First index is reserved for the fishes that will give birth at the end of the current turn
    
    Eg.: 3,4,3,1,2 will become:
    [0,  0,   1,   1,   2,   1,   0,   0,   0,   0]
     *  t(0) t(1) t(2) t(3) t(4) t(5) t(6) t(7) t(8)
    
    Parameters
    ----------
    inp : str
        The input string to parse
    
    Returns
    -------
    fishes : list[int]
        A fixed list of 10 integers
    """

    fishes = [0 for _ in range(10)]

    for fish_age in inp.split(','):
        fishes[int(fish_age) + 1] += 1
    
    return fishes

if __name__ == '__main__':
    main()