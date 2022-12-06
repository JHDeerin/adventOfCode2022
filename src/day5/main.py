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
    -   Actually, for parsing the stacks, can note that the stacks are in
        regular intervals - so once we know the exact number of stacks, then we
        know the exact index for a particular stack. We can get the number of
        stacks if we start at the bottom (which should help with builing the
        stacks anyway).

OUTCOME: TODO

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
import re
from typing import List, Tuple


def parse_initial_stacks(input: str) -> List[List[str]]:
    stacks = []
    for i, line in enumerate(reversed(input.splitlines())):
        if i == 0:
            num_stacks = (len(line) + 2)//4
            stacks = [[] for i in range(num_stacks)]
            continue
        for j in range(len(stacks)):
            try:
                char = line[j*4 + 1]
                if char.strip():
                    stacks[j].append(char)
            except IndexError:
                pass
    return stacks


def parse_move(input: str) -> Tuple[int, int, int]:
    """Move will be tuple of (n, src, dest)"""
    num_strs = re.findall(r"\d+", input)
    return [int(num_str) for num_str in num_strs]


def parse_moves(input: str) -> List[Tuple[int, int, int]]:
    moves = []
    for line in input.splitlines():
        moves.append(parse_move(line))
    return moves


def parse_stacks(input: List[str]) -> Tuple[List[List[str]], List[Tuple[int, int, int]]]:
    initial_stack_input, moves_input = "\n".join(input).split("\n\n")
    return parse_initial_stacks(initial_stack_input), parse_moves(moves_input)


def apply_moves(stacks: List[List[str]], moves: List[Tuple[int, int, int]]):
    for n, src, dest in moves:
        for i in range(n):
            stacks[dest-1].append(stacks[src-1].pop())


def part1(input: List[str]) -> str:
    stacks, moves = parse_stacks(input)
    apply_moves(stacks, moves)
    return "".join([stack[-1] for stack in stacks])


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
    assert result == "HNSNMTLHQ"

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
