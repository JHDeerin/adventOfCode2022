"""
Alright; for this problem, there are pairs of "elves" who are each assigned
a numerical range of floor sections to clean (e.g. "2-4" for sections 2,3,4).
The elf pairs are given as a string list of the ranges, e.g. "2-4,3-15"

For part 1, in how many of these pairs does one range entirely include another?
-   To do this, I'll need to first parse the range for each elf from the string,
    probably into a tuple (e.g. "2-4" -> (2,4)); then, for each elf pair, find
    if one range contains another
-   To check if one range contains another, can just check if the a.min <= b.min
    and if a.max <= b.max; HOWEVER, need to check this both ways to make sure
    the order doesn't matter (should still be O(1))

OUTCOME: Got it right! (459)

For part 2: We want to know ALL the pairs that have ANY overlap (not just
subsets)
-   This should be doable by just seeing if either min/max of one is within the
    range of the other (e.g. for "2-8,3-7", check 2 <= 3 <= 8 OR 2 <= 7 <= 8)

OUTCOME: Got the wrong answer at first (700 was too low). Trying again:
    -   Okay, my overlapping algorithm was clearly wrong; why?
        -   I was checking to see if the 2nd one's bounds were contained in the
            1st item, BUT this fails in the case that the 1st is a strict subset
            of the 2nd - so it would undercount. Shoot.
        -   Revising this and trying again...yup, that was the correct answer!
            (779)

REFLECTIONS:
-   Lesson: don't try to wing "I think this is probably correct" if I'm not
    confident, even if my solution passed the the example case (like my
    original second-part solution did). If I'm not confident my method/algo is
    correct, check it/test it where I'm unsure. (Of course I can have bugs even
    if I am confident, but trust my spidey-sense a bit).
-   Copy-pasting the input is a time sink; should try to read it from a file
    instead, since it's guaranteed to be a file every day.
    -   More generally, I can probably make a faily template that'll simplify
        things a bit by giving me some standard boilerplate
-   I over-genericized by writing logic to parse arbitrarily-large groups (not
    just pairs); I think that's mostly justified, but I probably could've
    recognized from the input file that the problem was restricting itself to
    pairs
-   For some reason hitting my "F2" key turns off the wifi; find out how to
    disable that, or make it require holding Fn or something?
"""
import re
from typing import List


def parse_section(section_str: str) -> List[int]:
    section = [int(num_match) for num_match in re.findall(r"\d+", section_str)]
    return section


def parse_groups(group_strs: List[str]) -> List[List[List[int]]]:
    groups = []
    for group_str in group_strs:
        group = [parse_section(section_str) for section_str in group_str.split(",")]
        groups.append(group)
    return groups


def is_contained_pair(pair: List[str]) -> bool:
    assert len(pair) == 2
    a, b = pair[0], pair[1]
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


def get_contained_pairs(group_strs: List[str]) -> int:
    pairs = parse_groups(group_strs)
    return len([pair for pair in pairs if is_contained_pair(pair)])


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert get_contained_pairs(test_input) == 2


def is_overlapping_pair(pair: List[str]) -> bool:
    assert len(pair) == 2
    a, b = pair[0], pair[1]
    a_overlaps_b = (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1])
    b_overlaps_a = (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1])
    return a_overlaps_b or b_overlaps_a


def get_overlapping_pairs(group_strs: List[str]) -> int:
    pairs = parse_groups(group_strs)
    return len([pair for pair in pairs if is_overlapping_pair(pair)])


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert get_overlapping_pairs(test_input) == 4


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()
    test_first_example()
    part1 = get_contained_pairs(input)
    print(f"part 1: {part1}")
    assert part1 == 459

    test_second_example()
    part2 = get_overlapping_pairs(input)
    print(f"part 2: {part2}")
    assert part2 == 779
