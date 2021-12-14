from itertools import product

'''  
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''


TEST_INPUT = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


TEST_INPUT_SHORT = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'''

'''
acedgfb
cdfbe
gcdfa
fbcad
dab
cefabd
cdfgeb
eafb
cagedb
ab

1. go from shortest segment (ab)
- since ab = number(1) then we know either a is top right and b bottom right or reverse (loop of 2)
2. dab
- since dab is number(7) then we know d must be top top
3. eafb
- since eafb is number(4) and we know top right a and bottom right is b, e and f must be middle and top left


'''


def main():
    
    segment_map = {
        0: 'abcefg',    # 6
        1: 'cf',        # 2
        2: 'acdeg',     # 5
        3: 'acdfg',     # 5
        4: 'bcdf',      # 4
        5: 'abdfg',     # 5
        6: 'abdefg',    # 6
        7: 'acf',       # 3
        8: 'abcdefg',   # 7
        9: 'abcdfg'     # 6
    }

    start_with = list(range(1,8))

    short_test_input = parse_input(TEST_INPUT_SHORT)

    for start in start_with:

    test_signal_patterns, test_output_values = parse_input(TEST_INPUT)
    
    with open('inputs/d8.txt') as f: 
        real_signal_patterns, real_output_values = parse_input(f.read())
    
    
    #print(num_unique_numbers_in_output(test_output_values))
    #print(num_unique_numbers_in_output(real_output_values))

    for signal_pattern in real_signal_patterns:
        print(signal_pattern)
    
def get_number_pattern_by_offset(offset: int = 0)

def num_unique_numbers_in_output(lst: list) -> int:
    return sum(len([v for v in r if len(v) in (2,3,4,7)]) for r in lst)

def parse_input(inp: str) -> tuple[list]:
    split_lines = inp.splitlines()
    if len(split_lines) >1:
        split_input = [line.split(' | ') for line in split_lines]
        signal_patterns = [x[0].split(' ') for x in split_input]
        output_values = [x[1].split(' ') for x in split_input]
    else:
        split_input = split_lines[0].split(' | ')
        signal_patterns = split_input[0].split(' ')
        output_values = split_input[1].split(' ') 

    return signal_patterns, output_values

if __name__ == '__main__':
    main()