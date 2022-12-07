"""
As we head to the star groves, the elves hand us a communication device. To communicate, we need to lock on to their signal - a squence of apparently-random characters one ata time. We receive the "datastream buffer"; we need to find the "start-of-packet" marker (which'll be the first sequence of 4 characters that are all different).

PART 1: How many characters need to be processed before the first start-of-packet marker? (min possible is four)

OUTCOME: Got it right! (1582)

PART 2: TODO

OUTCOME: Got it right! (3588)

REFLECTIONS: TODO
"""
from typing import List


def find_packet_start_index(input: str, marker_len: int) -> int:
    for i in range(marker_len,len(input)):
        if len(set(input[i-marker_len:i])) == marker_len:
            return i
    return None


def part1(input: str):
    packet_start_index = find_packet_start_index(input, marker_len=4)
    assert packet_start_index is not None
    return packet_start_index


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    print(part1(test_input))
    assert part1(test_input) == 7


def part2(input: str):
    packet_start_index = find_packet_start_index(input, marker_len=14)
    assert packet_start_index is not None
    return packet_start_index


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 19


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
