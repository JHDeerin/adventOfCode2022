"""
TODO

PART 1: TODO

OUTCOME: TODO

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
from typing import List


def part1(input: str):
    pass


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part1(test_input) == 0


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
