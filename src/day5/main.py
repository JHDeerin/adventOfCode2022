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

OUTCOME: Got it right! (HNSNMTLHQ)
-   The logic ended up taking me a second; I had a few bugs to iron out when
    initially parsing the stacks (out-of-range error w/ the indices, then
    forgetting to check if char was a space (and if so ignore it instead of
    adding it to a stack))

PART 2: Now, instead of moving 1 crate at a time, a move operation moves ALL the
crates at once while preserving their order. Find the same thing BUT with the
new movement behavior

OUTCOME: Got it right! (RNLFDJMCT)
-   This was much faster (I made one bug in the reversal logic but spotted it
    pretty quickly)

REFLECTIONS:
-   Keeping the parsed moves generic was a good idea (it let me quickly change
    the interpretation of what a move was)
-   The second part was very quick at <4 mins (although I could've moved faster
    if I was seriously going or speed - but I'm not racing anybody but myself
    here).
-   The first part, though, took up a lot of time - why?
    -   It took a bit for me to fully understand the problem; I think I was also
        intimidated for a sec on how to parse it, until I realized I could parse
        the first part from the bottom-up + jump straight to the right char
    -   From there, figuring out the algebra to get the correct char/number of
        stacks was slow for me to process for some reason (maybe just rusty at
        math?); I probably could've coded a regex solution faster (and it would
        be less brittle, although computationally slower ofc)
    -   Minor, but parsing the input from the get-go as separated lines made
        splitting the 2 different input parts harder; I had to rejoin them,
        split at the newline, and THEN go line-by-line again
-   I didn't use asserts to test intermediate assumptions, but instead did print
    debugging; that helped with some things (like seeing the empty char on the
    stack), but I think asserts are more reliable. Although both are slower than
    getting it all right the first time (but alas, I'm not powerful enough to
    gold it first try...usually)

-   Looking at the fastest coders' solutions:
    -   betaveros:
        -   Like me, he split the input into 2 parts at the newline (crates and
            moves)
        -   To avoid having to deal with spaces, he modified the input by
            putting a "." char on every blank line where the stack was supposed to be
        -   At the start, he just pre-allocated 9 stacks (since he saw there
            would never be more than that), instead of trying to count how many
            there were
        -   Then, when parsing the crates, he also started from the bottom-up,
            and in each line he filtered out everything except letters and dots
            (so he was guaranteed to have <# of stacks> items in every line).
            Then he just skipped the stacks with dots on that line
        -   He parsed the moves exactly like me (count, src, dest)
        -   He did a switch/case statement for the 2 parts; for the first part,
            similar to me (append to dst while popping from src - HOWEVER, he
            indexed from 1 to avoid having to do `i-1` statements)
        -   For the second part, he avoided needing a temporary variable; he
            just used array slicing to append to the dest, then remove from the
            source
                -   Does this work in Python? Let me check...yes, it does!
        -   Then, yup, got the last item in each list and string-joined 'em
            together.
            -   So, my approach was similar in spirit, but he was able to
                side-step a lot of the parsing complexity by guaranteeing the
                input would always have <# of stack> chars and by not trying to
                count the # of stacks in the first place
"""
import re
from typing import List, Tuple


def parse_initial_stacks(input: str) -> List[List[str]]:
    lines = input.splitlines()
    num_stacks = (len(lines[-1]) + 2)//4
    stacks: List[List[str]] = [[] for i in range(num_stacks)]
    # Throw out the last line, since we don't want to add it to the stack
    for line in reversed(lines[:-1]):
        for i in range(len(stacks)):
            try:
                char = line[i*4 + 1]
                if char.strip():
                    stacks[i].append(char)
            except IndexError:
                # Skip whitespace characters/out-of-range chars, indicating
                pass
    return stacks


def parse_move(input: str) -> Tuple[int, int, int]:
    """Move will be tuple of (n, src, dest)"""
    num_strs = re.findall(r"\d+", input)
    n, src, dest = [int(num_str) for num_str in num_strs]
    return n, src, dest


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


def apply_order_preserve_moves(stacks: List[List[str]], moves: List[Tuple[int, int, int]]):
    for n, src, dest in moves:
        stacks[dest-1] += stacks[src-1][-n:]
        stacks[src-1] = stacks[src-1][:-n]


def part1(input: List[str]) -> str:
    stacks, moves = parse_stacks(input)
    apply_moves(stacks, moves)
    return "".join([stack[-1] for stack in stacks])


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part1(test_input) == "CMZ"


def part2(input: List[str]) -> str:
    stacks, moves = parse_stacks(input)
    apply_order_preserve_moves(stacks, moves)
    return "".join([stack[-1] for stack in stacks])


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part2(test_input) == "MCD"


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
    assert result == "RNLFDJMCT"