"""
We need to collect "star"fruit by solving puzzles, so we can feed the reindeer
to give them magical powers. The elves are on an expedition to find the fruit.

The puzzle input is a list of how many calories each elf is carrying; each elf's
inentory is separated from the other elves by a blank line

PART 1: Find the elf with the most number of calories; how many calories are
they carrying?
-   Pretty easy; just parse each elf's inventory, then get the total number of
    calories, then get the max of that

OUTCOME: Got it right! (69501)

PART 2: The elves want to know the sum of the top 3 elves categories

OUTCOME: TODO

REFLECTIONS: TODO
"""
from typing import List


def parse_elf_inventories(input: List[str]) -> List[List[int]]:
    elf_inventories = []
    current_elf = []
    for item in input:
        try:
            current_elf.append(int(item))
        except ValueError:
            elf_inventories.append(current_elf)
            current_elf = []
    if current_elf:
        elf_inventories.append(current_elf)
    return elf_inventories


def part1(input: List[str]) -> int:
    elf_inventories = parse_elf_inventories(input)
    elf_calories = [sum(elf) for elf in elf_inventories]
    return max(elf_calories)


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part1(test_input) == 24000


def part2(input: List[str]):
    elf_inventories = parse_elf_inventories(input)
    elf_calories = [sum(elf) for elf in elf_inventories]
    return sum(sorted(elf_calories)[-3:])


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part2(test_input) == 45000


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")
    assert result == 69501

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
