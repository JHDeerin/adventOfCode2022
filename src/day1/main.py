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

OUTCOME: Got it right! (202346)
-   While doing this, though, I originally wasn't passing a test case;
    discovered a bug when I was reading in the list the first time (I was
    forgetting to add the last item - classic off-by-one error because I was
    parsing in each elf and ending when I reached a newline).
    -   I probably could've avoided this error by parsing a different way; maybe
        by parsing all the ints first (w/ blank lines as "-1") and THEN
        splitting the groups up based on that? Or by adding a blank line to the
        input to make sure nothing is a special case?

REFLECTIONS:
-   Process feels decently down; there are some micro-optimizations I could
    make, I'm sure, but I didn't have to write much more code than necessary
-   I don't like stateful parsing solutions, but I'm not sure how to do this
    one without it?
-   Completely unrelated, but betaveros (one of the best Advent of Code
    speedcoders) is doing the challenge in his own language
    (https://github.com/betaveros/advent-of-code-2022), and recommended
    "Crafting Interpreters" by Bob Nystrom (the same guy who wrote the awesome
    "Game Programming Patterns" book that I really need to finish)
        -   Holy cow, his solution is 7 lines long (I know it's designed as a
            code golfing language, and he did say he cleans up his solutions
            before posting, but still!)
        -   Okay, his functional solution (as far as I can tell) was to read the
            whole thing in as a string, split wherever there were 2 newlines in
            a row, parse everything remaining into integers, then sum them
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
