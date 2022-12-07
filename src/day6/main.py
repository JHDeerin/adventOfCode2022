"""
As we head to the star groves, the elves hand us a communication device. To
communicate, we need to lock on to their signal - a squence of
apparently-random characters one ata time. We receive the "datastream buffer";
we need to find the "start-of-packet" marker (which'll be the first sequence of
4 characters that are all different).

PART 1: How many characters need to be processed before the first
start-of-packet marker? (min possible is four)

OUTCOME: Got it right! (1582)

PART 2: What about if the starting packet sequence was 14 characters?

OUTCOME: Got it right! (3588)

REFLECTIONS:
-   That went great! I solved both parts in <10 minutes with no real bugs (I
    had an off-by-n error at first because I forgot I was already starting from
    and index >0 when looking for a packet)
    -   I happened to choose the perfect variable that the problem went for: the
        packet length to search for (if it had been something like the same
        length of 4 but '2 characterss matching', the set still would've helped
        me pivot quickly)
    -   It was basically a sliding window problem, which I recognized, so that
        made it quick to think about; it was clear how to solve it
-   Having the input be a string instead of a list of strings is another point
    in favor of making the default input type just being a raw string; let's
    go with that. I'll edit the template.
-   Having the asserts just fail and not print out more details is annoying;
    is there a way to have pytest-style asserts?
-   Looking at other solutions:
    -   Betaveros did the exact same thing as I did (sliding window, compare
        the set size to the size of the window); his solution was a one-liner,
        though
    -   Oliver-ni did even more literally the exact same thing I did (literally
        the exact same syntax, just different variable names)

"""
def find_packet_start_index(input: str, marker_size: int) -> int:
    for i in range(marker_size, len(input)):
        if len(set(input[i-marker_size:i])) == marker_size:
            return i
    return None


def part1(input: str):
    packet_start_index = find_packet_start_index(input, marker_size=4)
    assert packet_start_index is not None
    return packet_start_index


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part1(test_input) == 7


def part2(input: str):
    packet_start_index = find_packet_start_index(input, marker_size=14)
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
    assert result == 1582

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
    assert result == 3588
