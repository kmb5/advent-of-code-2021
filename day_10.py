from queue import LifoQueue

TEST_INPUT = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


BRACKET_MATCHES = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def main():
    
    brackets = LifoQueue()
    error_points = 0

    with open('inputs/d10.txt') as f:
        inp = f.read().splitlines()

    for row in inp:
        for i in row:
            if i in BRACKET_MATCHES:
                # opening bracket
                brackets.put(i)
            else:
                last = brackets.get()
                if i != BRACKET_MATCHES[last]:
                    print(f'Expected {BRACKET_MATCHES[last]}, found {i}')
                    error_points += POINTS[i]
    
    print(error_points)


        






if __name__ == '__main__':
    main()