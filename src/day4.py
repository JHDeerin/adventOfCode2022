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
    test_first_example()
