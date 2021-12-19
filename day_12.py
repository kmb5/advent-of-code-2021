from collections import defaultdict

TEST_INPUT = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

def main():

    test_input = TEST_INPUT.splitlines()

    graph = defaultdict(list)

    for row in test_input:
        a, b = row.split('-')
        graph[a].append(b)
    


    


if __name__ == '__main__':
    main()