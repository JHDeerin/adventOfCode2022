"""
A basic rope simulation: a rope has a head and a tail, and if the head moves far enough away, the tail follows. The head and tail must always be touching (adjacent, diagonal, or overlapping if just "H" on-screen). A 2D grid shows their positions. If the head moves so that it's not touching, the tail follows behind (diagonal ones move so they become adjacent). There are 4 ways the head can move: (U)p, (D)own, (R)ight, (L)eft

PART 1: Assuming we start with the head and tail overlapping, how many distinct positions does the tail visit as the head moves?
- Will represent a 2D grid and the head + tail position; then, if the tail is more than 2 away, will "snap" the tail to the right position
    -   Can tell the tail is far enough away if abs(tail.x - head.x) > 1 or (tail.y - head.y) > 1 (works for diagonals as well)
    -   To get the unique positions, record all the tail movements x/y tuples (or row/col?), then take the set


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
    assert part1(test_input) == 13


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
