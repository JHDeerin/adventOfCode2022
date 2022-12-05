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
    assert len(pairs[0]) == 2
    return len([pair for pair in pairs if is_contained_pair(pair)])


def test_first_example():
    input_pairs = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    assert get_contained_pairs(input_pairs) == 2


if __name__ == "__main__":
    input = [

    ]
    test_first_example()
