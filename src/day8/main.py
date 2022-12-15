"""
We get a 2D map representing the height of trees in an area (represented from 0 to 9, a single digit). We say a tree is "visible" if all the trees in one direction (up to the edge of the grid) are shorter than it (so, all trees at the edge of the grid are obviously visible).

PART 1: How many trees are visible from outside the grid?
- Parse the grid into a 2D array
- Then, iterate over each tree and find if it's visible (just go in each)

OUTCOME: Got it! (1814)

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
from typing import List


def get_grid(input: str) -> List[List[int]]:
    rows = []
    for line in input.splitlines():
        row = [int(char) for char in line]
        rows.append(row)
    return rows


def is_visible(grid: List[List[int]], row: int, col: int) -> bool:
    if (not (0 < row < len(grid))) or (not (0 < col < len(grid[0]))):
        return True
    tree_height = grid[row][col]
    # Get the heights in the row + col not including the tree itself
    left_heights = grid[row][0:col]
    right_heights = grid[row][col+1:]
    above_heights = [grid[i][col] for i in range(row)]
    below_heights = [grid[i][col] for i in range(row+1, len(grid))]

    for heights in [left_heights, right_heights, above_heights, below_heights]:
        shorter = [x for x in heights if x < tree_height]
        if len(shorter) == len(heights):
            return True

    return False


def get_num_trees_visible(grid: List[List[int]]) -> int:
    num_visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_visible(grid, row, col):
                num_visible += 1
    return num_visible


def part1(input: str) -> int:
    grid = get_grid(input)
    return get_num_trees_visible(grid)


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
    assert result == 1814

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
