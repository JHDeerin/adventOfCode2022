"""
We get a 2D map representing the height of trees in an area (represented from 0 to 9, a single digit). We say a tree is "visible" if all the trees in one direction (up to the edge of the grid) are shorter than it (so, all trees at the edge of the grid are obviously visible).

PART 1: How many trees are visible from outside the grid?
- Parse the grid into a 2D array
- Then, iterate over each tree and find if it's visible (just go in each)

OUTCOME: TODO

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
from typing import List


def part1(input: str) -> int:
    grid = get_grid(input)
    pass


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part1(test_input) == 21


def part2(input: str):
    pass


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 0


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
