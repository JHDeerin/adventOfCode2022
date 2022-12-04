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
"""

def test_example_problem():
    input_rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert get_item_priority_sum(input_rucksacks) == 157


if __name__ == "__main__":
    test_example_problem()
