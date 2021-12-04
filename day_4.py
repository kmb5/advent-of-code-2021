from typing import Tuple
from enum import Enum

TEST_INPUT = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''


def main():

    with open('inputs/d4.txt') as f:
        real_input = f.read()

    test_inp, test_boards = read_input(TEST_INPUT)
    real_inp, real_boards = read_input(real_input)

    test_winning_score = check_first_winning_board_score(test_inp, test_boards)
    print(f'Part 1 test solution: {test_winning_score}')

    real_winning_score = check_first_winning_board_score(real_inp, real_boards)
    print(f'Part 1 test solution: {real_winning_score}')

    test_last_winning_score = check_last_winning_board_score(test_inp, test_boards)
    print(f'Part 2 test solution: {test_last_winning_score}')
    
    real_last_winning_score = check_last_winning_board_score(real_inp, real_boards)
    print(f'Part 2 test solution: {real_last_winning_score}')


class BingoBoard:
    """Represents a Bingo Board

    Parameters
    ----------
    numbers : list[list[int]]
        A 2d list of integers representing the numbers on the board
    """
    
    def __init__(self, numbers: list[list[int]]) -> None:
        self.numbers = numbers
        self.num_rows = len(numbers)
        self.num_cols = len(numbers[0])
        # Initialize a 2d array of zeros to store numbers that have been found
        self.marked_numbers = [[0 for _ in row] for row in numbers]
        self.is_won = False
    
    def __repr__(self) -> str:
        """Return a string where each 'marked' (=found) number is green and all others are red
        
        Returns
        -------
        repr : str
            The string representation of the object
        """
        repr = '\n'
        for i, row in enumerate(self.numbers):
            row_repr = ''
            for j, num in enumerate(row):
                color = Color.GREEN if self.marked_numbers[i][j] == 1 else Color.RED  
                row_repr += _colorize(str(num), color) + '\t'
            repr += row_repr + '\n'
        return repr
    
    def check_for_number(self, number: int) -> None:
        """Check if a number is present in our board. If yes, add it to marked numbers

        Parameters
        ----------
        number : int
            The number to check for
        """

        if self.is_won:
            # Don't do anything if we already won
            return

        for i, row in enumerate(self.numbers):
            for j, num in enumerate(row):
                if num == number:
                    self.marked_numbers[i][j] = 1

        self.check_win()
    
    def check_win(self) -> None:
        """Check if any horizontal or vertical line in the marked numbers is all true
        If yes, it means this board won, so we set the is_won parameter to True
        """
        #            ONE OF THE ROWS WON                                  ONE OF THE COLS WON
        if (any(all(row) for row in self.marked_numbers)) or (any(all(x) for x in list(zip(*self.marked_numbers)))):
            self.is_won = True 
    
    def get_all_unmarked_numbers(self) -> list:
        """Get a list of numbers that are unmarked (= have not been found yet)
        
        Returns
        -------
        all_unmarked : list
            A list of numbers that have not been found yet
        """

        all_unmarked = []
        for i, row in enumerate(self.numbers):
            for j, num in enumerate(row): 
                if self.marked_numbers[i][j] == 0:
                    all_unmarked.append(num)
        return all_unmarked


class Color(Enum):
    """Enum to represent ANSI color codes"""
    RESET = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'


def check_first_winning_board_score(inp: list, boards: list[BingoBoard]) -> int:
    """Play rounds of Bingo with the inp list on all the boards
    and return the score of the first board that won
    
    Parameters
    ----------
    inp : list
        The list of numbers to play
    boards : list[BingoBoard]
        A list of BingoBoards to play on
    
    Returns
    -------
    winning_score : int
        The sum of all unmarked numbers on the winning board
        multiplied by the number that was just called when the board won
    """

    for number in inp:
        for board in boards:
            board.check_for_number(number)
            if board.is_won:
                print(board)
                return sum(board.get_all_unmarked_numbers()) * number


def check_last_winning_board_score(inp: list, boards: list[BingoBoard]) -> int:

    winning_boards = []
    last_winning_number = 0

    for number in inp:
        for board in boards:
            if not board.is_won:
                # if board is already won, skip, otherwise check number
                board.check_for_number(number)
                if board.is_won:
                    # if board just won in this step
                    winning_boards.append(board)
                    last_winning_number = number
    
    print(winning_boards[-1])
    return sum(winning_boards[-1].get_all_unmarked_numbers()) * last_winning_number

def read_input(inp: str) -> Tuple[list, list[BingoBoard]]:
    """Read the input string and return a tuple consisting of:
    1. The list of inputs for the bingo
    2. The list of BingoBoards to play on
    
    Parameters
    ----------
    inp : str
        The input to parse
    
    Returns
    (input_numbers, boards) : Tuple[list, list[BingoBoard]]
        The inputs and the boards to play on
    """

    inp_list = inp.split('\n\n')
    input_numbers = [int(x) for x in inp_list[0].split(',')]
    boards = []

    for board_nums in inp_list[1:]:
        b = [[int(x) for x in b.split()] for b in board_nums.split('\n')]
        boards.append(BingoBoard(b))

    return input_numbers, boards


def _colorize(text: str, color: Color) -> str:
    """Helper function to colorize a string
    
    Parameters
    ----------
    text : str
        The text to colorize
    color : Color
        The color to use
    
    Returns
    -------
    str
        The colorized text
    """

    return color.value + text + Color.RESET.value


if __name__ == '__main__':
    main()