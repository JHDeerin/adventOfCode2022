"""
A basic rope simulation: a rope has a head and a tail, and if the head moves far enough away, the tail follows. The head and tail must always be touching (adjacent, diagonal, or overlapping if just "H" on-screen). A 2D grid shows their positions. If the head moves so that it's not touching, the tail follows behind (diagonal ones move so they become adjacent). There are 4 ways the head can move: (U)p, (D)own, (R)ight, (L)eft

PART 1: Assuming we start with the head and tail overlapping, how many distinct positions does the tail visit as the head moves?
- Will represent a 2D grid and the head + tail position; then, if the tail is more than 2 away, will "snap" the tail to the right position
    -   Can tell the tail is far enough away if abs(tail.x - head.x) > 1 or (tail.y - head.y) > 1 (works for diagonals as well)
    -   To get the unique positions, record all the tail movements x/y tuples (or row/col?), then take the set


OUTCOME: Got it right! (6284) (Had a stupid bug where I typed one of the direction keys wrong)

PART 2: The rope is now 10 knots long; the 1st knot is the head, the 2nd follows the 1st as its head, the 3rd follows the 2nd as its head, etc. Find how many the new "tail" (the 10th knot) visits.
- Okay, so now, I want to pass in a list of "rope" positions, move the first one, and then update the rest

OUTCOME: Got it wrong the first time with 2639 (too low - didn't use both test cases - but the 2nd test case still passed!?WTF!?)
-   Okay, the head moved to 7103 positions - so the right answer is between 2640 and 7103...
-   Okay, printing out a visualization shows me that there are some disconnected islands where the tail somehow "jumped" and skipped a space...hmmm
    -   I guess my "snapping" logic somehow breaks down in some cases where multiple pieces shift at once? If I change the rope to instead just move 1 in the right direction, does that fix things?

REFLECTIONS: TODO
"""
from typing import List, Tuple


direction_deltas = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


def get_movements(input: str) -> List[Tuple[int, int]]:
    movements = []
    for line in input.splitlines():
        direction, magnitude = line[0], int(line[2:])
        movements += [direction_deltas[direction] for _ in range(magnitude)]
    return movements


def snap_tail(head: Tuple[int, int], tail: Tuple[int, int],) -> Tuple[int, int]:
    x_diff, y_diff = head[0] - tail[0], head[1] - tail[1]
    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return tail
    # Snap tail to closest head position
    if abs(x_diff) >= 2:
        # negative x_diff means tail is to the right, else to the left
        return (head[0] + 1, head[1]) if x_diff < 0 else (head[0] - 1, head[1])
    # negative y_diff means tail is above, else below
    return (head[0], head[1] + 1) if y_diff < 0 else (head[0], head[1] - 1)


def play_movements(
    moves: List[Tuple[int, int]],
    knots: List[Tuple[int, int]]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    head_positions, tail_positions = [knots[0]], [knots[-1]]
    for move in moves:
        for i, knot in enumerate(knots):
            if i == 0:
                knots[i] = (knot[0] + move[0], knot[1] + move[1])
                continue
            knots[i] = snap_tail(knots[i-1], knot)
        head_positions.append(knots[0])
        tail_positions.append(knots[-1])
    return head_positions, tail_positions


def test_snap_tail():
    assert snap_tail((0,0), (0,0)) == (0,0)
    assert snap_tail((0,0), (1,1)) == (1,1)
    # above
    assert snap_tail((0,0), (1,2)) == (0,1)
    # below
    assert snap_tail((0,0), (1,-2)) == (0,-1)
    # left
    assert snap_tail((0,0), (-2,-1)) == (-1,0)
    # right
    assert snap_tail((0,0), (2,-1)) == (1,0)


def part1(input: str) -> int:
    head_pos, tail_pos = (0,0), (0,0)
    movements = get_movements(input)
    head_positions, tail_positions = play_movements(movements, [head_pos, tail_pos])
    return len(set(tail_positions))


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    print(part1(test_input))
    assert part1(test_input) == 13


def print_tail_traversed_paths(tail_positions: List[Tuple[int, int]]):
    min_x, max_x = min([x[0] for x in tail_positions]), max([x[0] for x in tail_positions])
    min_y, max_y = min([y[1] for y in tail_positions]), max([y[1] for y in tail_positions])

    unique_tail_pos = set(tail_positions)
    print(f"{len(unique_tail_pos)} tail pos | x: {min_x} to {max_x} | y: {min_y} to {max_y}")
    print("=" * 40)
    for y in range(max_y, min_y-1, -1):
        chars = []
        for x in range(min_x, max_x+1):
            char = "."
            if (x,y) == (0,0):
                char= "s"
            elif (x,y) in unique_tail_pos:
                char = "#"
            chars.append(char)
        print("".join(chars))


def part2(input: str) -> int:
    knots = [(0,0)] * 10
    movements = get_movements(input)
    head_positions, tail_positions = play_movements(movements, knots)
    print_tail_traversed_paths(tail_positions)
    return len(set(tail_positions))


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 1


def test_third_example():
    with open("test2.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 36


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    assert get_movements("R 4") == [(1, 0), (1, 0), (1, 0), (1, 0)]
    test_snap_tail()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")
    assert result == 6284

    test_second_example()
    test_third_example()

    result = part2(input)
    print(f"part 2: {result}")
