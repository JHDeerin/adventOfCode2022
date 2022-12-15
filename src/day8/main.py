"""
We get a 2D map representing the height of trees in an area (represented from 0 to 9, a single digit). We say a tree is "visible" if all the trees in one direction (up to the edge of the grid) are shorter than it (so, all trees at the edge of the grid are obviously visible).

PART 1: How many trees are visible from outside the grid?
- Parse the grid into a 2D array
- Then, iterate over each tree and find if it's visible (just go in each)

OUTCOME: Got it! (1814) (did waste time on a misunderstanding, trying to find the visibility for a whole row instead of the halves of the row separately)

PART 2: The elves want a scenic view; find the max "scenic score" for a tree (the distances it can see in all 4 directions, multiplied).

OUTCOME: Got it right! (330786)

REFLECTIONS:
-   Both parts took too long (40 minutes total; part 1 took 20 minutes, part 2 took 15 - which it really shouldn't have)
-   Got really slowed down by 2 bugs:
    -   In part 1, I forgot to check the visibility in a single direction
    -   In part 2, I reversed the wrong list, throwing off my answer
    -   Checking a 2D line threw my brain for a loop for some reason; I don't think I did this cleanly (feels like there has to be a more efficient way)
-   Intermediate test cases for individual trees would've helped
-   Looking at other people's solutions:
    - betaveros
        -   Having trouble actually understanding his solution; same basic idea of have a function that gets the "rays" (the heights of the trees in the 4 directions - implements them in some interesting language-specific way where he defines the delta and iterates to the end of the grid), but then he does it in a functional style where for each of those "rays" he checks if all of a ray is under the current height, then does any() to get them all together. He then iterates over the whole map w/ a double for-loop to get a list of booleans and sums them
        - For the 2nd part, he takes the max of a double-for loop again, and this time for all the rays in the 4 directions marches 1, breaks when the height is >= to the current tree, then does the product (similar to my solution but more concise)
    -   oliver-ni
        -   First part was very similar ot my solution; read the grid, iterated over rows/cols, then in the 4 directions like how I did, but then used Python's all() + or function to check visibility for each direction
        -   For the 2nd part, I actually think I had a cleaner solution (he did the same thing, but without the reversal, and he had 4 for loops)
"""
from math import prod
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


def scenic_score(grid: List[List[int]], row: int, col: int) -> int:
    tree_height = grid[row][col]

    left_heights = grid[row][0:col]
    right_heights = grid[row][col+1:]
    above_heights = [grid[i][col] for i in range(row)]
    below_heights = [grid[i][col] for i in range(row+1, len(grid))]

    # reverse left/above so the 1st index is closest tree
    left_heights.reverse()
    above_heights.reverse()

    direction_scores = []
    for heights in [left_heights, right_heights, above_heights, below_heights]:
        trees_visible = 0
        for height in heights:
            trees_visible += 1
            if height >= tree_height:
                break
        direction_scores.append(trees_visible)
    print(direction_scores)
    return prod(direction_scores)


def get_scenic_scores(grid: List[List[int]]) -> List[int]:
    scores = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            scores.append(scenic_score(grid, row, col))
    return scores


def part2(input: str):
    grid = get_grid(input)
    scenic_scores = get_scenic_scores(grid)
    return max(scenic_scores)


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    print(part2(test_input))
    assert part2(test_input) == 8


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
    assert result == 330786
