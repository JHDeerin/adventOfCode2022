"""
Alright - for this challenge, there's a bunch of "items" (ASCII chars, a-z and
A-Z) in "rucksacks" (strings). For each "rucksack", there's exactly 1 item that
appears  in both the 1st/2nd half of each rucksack (so I guess we can assume
all the strings have an even-numbered length?). The goal: find all of these
characters, then get the sum of their values (1-26 for lowercase a-z, 27-52 for
A-Z).

So, basically, find the letter that occurs in both halves of a string, do that
for all the strings, then get the correct value of each letter and sum them up.

Ideas:
-   The value of an "item" can be gotten pretty trivially by checking if the
    letter is uppercase or lowercase (convert it to its numeric ASCII value
    and check the range - or, alternatively, see if char.lower() == char). Then,
    we can just take the letter's ASCII value minus whatever offset is appropriate for the uppercase/lowercase. Should be O(1)
-   For finding the duplicate letter, split the string in half, get the set of
    letters in each half, then take the intersect of the sets - there should be
    exactly 1 item that both halves share.

EDIT: There's a second half to the problem! Here, each group of 3 "rucksacks"
(i.e. strings) is carried by a group of elves, who should share exactly 1
"badge" item in all their rucksacks - i.e. we're doing the same problem, but
finding the 1 item shared between all 3 rucksacks (instead of 2 halves of the
same rucksack).

So, changes required to do this will be to find the shared item between 3 groups
instead of just 2, and to change the group creation logic to be "3 groups of
rucksacks" instead of "2 groups in a single rucksack". Make the intersection
code more generic, and change the grouping. Should be fairly easy.

OUTCOME:
-   Got the first half right with 7763! Wait...that was just the first half?
-   Got the second half right, too! (2569)
"""
from functools import reduce
from typing import List, Set


def get_shared_items(item_groups: List[str]) -> Set[str]:
    assert len(item_groups) > 1
    unique_item_groups = [set(group) for group in item_groups]
    shared_items = reduce(lambda a,b: a.intersection(b), unique_item_groups)
    return set(shared_items)


def get_misplaced_item(rucksack: str) -> str:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]

    shared_items = get_shared_items([compartment1, compartment2])
    assert len(shared_items) == 1
    return shared_items.pop()


def item_priority(item: str) -> int:
    assert len(item) == 1
    is_capital_letter = item < "a"
    if is_capital_letter:
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    return priority


def get_item_priority_sum(rucksacks: List[str]) -> int:
    misplaced_items = [get_misplaced_item(rucksack) for rucksack in rucksacks]
    return sum(item_priority(item) for item in misplaced_items)


def test_first_example_problem():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert get_item_priority_sum(test_input) == 157


def get_badge_item(rucksacks: List[str]) -> str:
    shared_items = get_shared_items(rucksacks)
    assert len(shared_items) == 1
    return shared_items.pop()


def get_badge_priority_sum(rucksacks: List[str], elf_group_size: int=3) -> int:
    def _group(items: list, n: int) -> List[tuple]:
        return [items[i:i+n] for i in range(0, len(items), n)]

    badge_items = [
        get_badge_item(group) for group in _group(rucksacks, elf_group_size)
    ]
    return sum(item_priority(item) for item in badge_items)


def test_second_example_problem():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert get_badge_priority_sum(test_input) == 70


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

    test_first_example_problem()
    priority_sum = get_item_priority_sum(input)
    print(f"Misplaced items' priority sum: {priority_sum}")
    assert priority_sum == 7763

    test_second_example_problem()
    priority_sum = get_badge_priority_sum(input)
    print(f"Badge items' priority sum: {priority_sum}")
    assert priority_sum == 2569
