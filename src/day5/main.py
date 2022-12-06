"""
Towers-of-Hanoi style, there are some stacks of crates that are moved between
each other. The initial stack configuration and the steps taken are written in
a text file. Crates are moved one at a time, starting from the top of the stack
(i.e. just like a normal stack data structure).

The "crates" are represented as single-char inside braces, like so: `[x]`.

PART 1: Find the crates at the top of each stack.
-   The parsing from the file is a bit tricky (because we have to parse stuff
    in a horizontal direction as well), but after that it's just parsing each
    move and popping/adding stuff to a stack.
-   For the parsing, can split the file at the newline; then, parse initial
    stacks from the first part (before the newline), and then parse the moves
    from the second part.

OUTCOME: TODO

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
from typing import List


def part1(input: List[str]):
    pass


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part1(test_input) == "CMZ"


def part2(input: List[str]):
    pass


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part2(test_input) == 0


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
