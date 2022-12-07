"""
As we head to the star groves, the elves hand us a communication device. To communicate, we need to lock on to their signal - a squence of apparently-random characters one ata time. We receive the "datastream buffer"; we need to find the "start-of-packet" marker (which'll be the first sequence of 4 characters that are all different).

PART 1: How many characters need to be processed before the first start-of-packet marker? (min possible is four)

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
    assert part1(test_input) == 7


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
