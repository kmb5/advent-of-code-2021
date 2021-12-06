from __future__ import annotations
from typing import Union

def main():
    
    with open('inputs/d6.txt') as f:
        fishes = [int(x) for x in f.read().split(',')]

    fish_school = LanternfishSchool(fishes)
    
    for day in range(1, 81):
        fish_school.pass_day()
        print(f'After {day} day: {len(fish_school)}')
    
    print(len(fish_school))

class Lanternfish():
    """Represents a lanternfish which will spawn a new lanternfish
    when it's timer is at -1
    
    Parameters
    ----------
    days_until_spawn : int
        Will spawn a new Lanternfish when it hits 0
    """

    def __init__(self, days_until_spawn: int = 8) -> 0:
        self.days_until_spawn = days_until_spawn
    
    def spawn(self) -> Union[None, Lanternfish]:
        """Spawn a new instance if days until spawn is at -1
        and then reset days until spawn to 6
        
        Returns
        -------
        - None if days_until_spawn is not -1
        - a new Lanternfish instance if it is
        """

        if self.days_until_spawn == -1:
            self.days_until_spawn = 6
            return Lanternfish()

        
    def decrease_days_until_spawn(self, by: int = 1) -> None:
        """Decreases days until spawn by the number given
        
        Parameters
        ----------
        by : int
            Number to decrease days_until_spawn by (default 1)
        """

        self.days_until_spawn -= by

    
    def __repr__(self):
        return self.days_until_spawn
    

class LanternfishSchool():
    """Represents a group of Lanternfishes
    (fun fact - a group of fishes is called a 'school')

    Parameters
    ----------
    fish_days : list[int]
        A list with the initial fishes' days_until_spawn
    """

    def __init__(self, initial_fish_days: list[int]) -> None:
        self.fishes = []

        for day in initial_fish_days:
            self.fishes.append(Lanternfish(day))
        
    def pass_day(self) -> None:
        """For each day, decrease each fishes days_until_spawn by 1
        and handle spawning new fishes"""

        spawned_fishes = []
        for fish in self.fishes:
            fish.decrease_days_until_spawn()
            spawned = fish.spawn()
            if spawned:
                spawned_fishes.append(spawned)
        
        # Append at end of the day because we don't want to already
        # decrease the days_until_spawn for these fishes
        self.fishes += spawned_fishes
    
    
    def __repr__(self):
        return (',').join(str(x.days_until_spawn) for x in self.fishes)
    
    
    def __len__(self):
        return len(self.fishes)

if __name__ == '__main__':
    main()