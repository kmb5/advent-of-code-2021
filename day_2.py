TEST_INPUT = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

def main():
    
    test_input = _parse_input(TEST_INPUT)
    with open('inputs/d2.txt') as f:
        real_input = _parse_input(f.read())

    # Part 1
    submarine = Submarine()

    submarine.move_multiple(test_input)
    print(f'Part 1 test solution: {submarine.calculate_position_depth_multiple()}')

    submarine.reset()
    submarine.move_multiple(real_input)
    print(f'Part 1 solution: {submarine.calculate_position_depth_multiple()}')

    # Part 2
    advanced_submarine = AdvancedSubmarine()

    advanced_submarine.move_multiple(test_input)
    print(f'Part 2 test solution: {advanced_submarine.calculate_position_depth_multiple()}')

    advanced_submarine.reset()
    advanced_submarine.move_multiple(real_input)
    print(f'Part 2 solution: {advanced_submarine.calculate_position_depth_multiple()}')


class Submarine():
    """Represents a submarine that can move forward, down or up"""

    def __init__(self, pos_h: int = 0, depth: int = 0) -> None:
        self.pos_h = pos_h # horizontal position
        self.depth = depth
    
    def move(self, direction: str, amount: int) -> None:
        """Moves the submarine in the given direction by the given amount
        
        Parameters
        ----------
        direction : str
            The direction to move to
        amount : int
            Amount of 'steps' to move
        
        Raises
        ------
        ValueError
            If direction is not valid
        """

        if direction == 'forward':
            self.pos_h += amount
        elif direction == 'up':
            self.depth -= amount
        elif direction == 'down':
            self.depth += amount
        else:
            raise ValueError('Direction has to be forward, up or down!')
    
    def move_multiple(self, moves: list[tuple]) -> None:
        """Move the submarine multiple steps
        
        Parameters
        ----------
        moves : list[tuple]
            A list of tuples for each move - (direction, amount)
        """

        for row in moves:
            self.move(row[0], row[1])
    
    def calculate_position_depth_multiple(self) -> int:
        """Return position multiplied by depth
        
        Returns
        -------
        int
            Position multiplied by depth
        """

        return self.pos_h * self.depth
    
    def reset(self) -> None:
        """Resets the submarine to the base position"""
        self.pos_h = 0
        self.depth = 0
        

class AdvancedSubmarine(Submarine):
    """Represents an advanced submarine that can move forward, down or up 
    in relation to its current aim"""

    def __init__(self, pos_h: int = 0, depth: int = 0, aim: int = 0):
        self.aim = aim
        super().__init__(pos_h, depth)
    
    def move(self, direction: str, amount: int) -> None:
        """Moves the submarine in the given direction by the given amount
        
        Parameters
        ----------
        direction : str
            The direction to move to
        amount : int
            Amount of 'steps' to move
        
        Raises
        ------
        ValueError
            If direction is not valid
        """

        if direction == 'forward':
            self.pos_h += amount
            self.depth += self.aim * amount
        elif direction == 'up':
            self.aim -= amount
        elif direction == 'down':
            self.aim += amount
        else:
            raise ValueError('Direction has to be forward, up or down!')
    
    def reset(self):
        """Resets the submarine to the base position"""
        self.pos_h = 0
        self.depth = 0
        self.aim = 0


def _parse_input(inp: str) -> list[tuple]:
    """Helper function to turn the input into a list of tuples
    where each tuple represents a move direction and a move amount
    
    Parameters
    ----------
    inp : str
        The input to parse
    
    Returns:
    list[tuple]
        A list of tuples representing the moves to make
    """

    inp_lst = [line.split() for line in inp.splitlines()]
    return [(x[0], int(x[1])) for x in inp_lst]


if __name__ == '__main__':
    main()