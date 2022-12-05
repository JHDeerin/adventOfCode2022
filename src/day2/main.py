"""
Okay, we're playing rock paper scissors, where the text file gives the move
our opponent will play (A=rock, B=paper, C=scissors - see below) and our
response. We get a certain number of points each round based on the outcome and
what shape we played.

PART 1: Calculate the total number of points we'd get if we follow the guide
exactly.
-   This is just parsing everything and then calculating the score correctly; no
    biggie.

OUTCOME: Got it right! (13484)

PART 2: It turns out the 2nd letter is ACTUALLY what outcome the round needs,
and we need to pick the correct shape based on what our opponent played.
-   How to do this? Basically, I'll hardcode every possible case

OUTCOME: Got it right! (13433)

REFLECTIONS:
-   Like in the actual problem, assuming the meaning of the 2nd row meant I
    was caught flat-footed when the meaning changed, and I had to rewrite the
    function (or, in my case, copy-paste it). Not sure if this was avoidable
    or not
-   The way I coded the wins/needed moves feels inelegant; clean this up? How
    can I do this without hardcoding everything?
    -   It seems like we could derive this if we knew the rules of the game; the
        minimum needed rules are "rock > scissors", "scissors > paper",
        "paper > rock", and matches are ties (4 items).
        -   This could be represented by a dictionary of items and their counter
            (kind of like pokemon weaknesses)
    -   So, I think the "get round outcome" function is actually pretty ideal
    -   The "get needed shape", then, could be derived by saying:
        -   If we need a tie, return the same item
        -   If we need a win, look up the item's counter
        -   If we need a loss, invert the dictionary and look up the item
    -   I think that's the best we could do? (Maybe explore some other
        solutions people came up with)
-   I think the dictionaries w/ the meanings was an overall win
-   Copy the input AND the test input right away to avoid weird errors
-   Tests should have asserts from the get-go to avoid having to type them in
-   Input files shouldn't have a newline at the end (certainly not by default)
-   This was faster (~35 minutes to solve both parts), but it was also an easier
    problem IMO
"""
from typing import List, Tuple


opponent_shape = {
    "A": "R",
    "B": "P",
    "C": "S",
}


response_shape = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}


response_outcome = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


shape_scores = {
    "R": 1,
    "P": 2,
    "S": 3,
}

outcome_scores = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}


def parse_shape(move: str) -> str:
    assert len(move) == 1
    return opponent_shape.get(move, response_shape.get(move))


def parse_rounds(round_strs: List[str]) -> Tuple[str, str]:
    rounds = []
    for round_str in round_strs:
        plays = round_str.split()
        rounds.append((parse_shape(plays[0]), parse_shape(plays[1])))
    return rounds


def get_round_outcome(round: Tuple[str, str]) -> str:
    if round[0] == round[1]:
        return "draw"
    if round[0] == "R" and round[1] == "P":
        return "win"
    if round[0] == "P" and round[1] == "S":
        return "win"
    if round[0] == "S" and round[1] == "R":
        return "win"
    return "lose"


def get_round_score(round: Tuple[str, str]) -> int:
    return shape_scores[round[1]] + outcome_scores[get_round_outcome(round)]


def get_round_scores(rounds: List[Tuple[str, str]]) -> List[int]:
    return [get_round_score(round) for round in rounds]


def part1(input: List[str]):
    rounds = parse_rounds(input)
    return sum(get_round_scores(rounds))


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part1(test_input) == 15


def get_needed_shape(shape: str, outcome: str) -> str:
    # TODO: What's a more elegant way to do this?
    if outcome == "win":
        if shape == "R":
            return "P"
        if shape == "P":
            return "S"
        if shape == "S":
            return "R"
    if outcome == "lose":
        if shape == "R":
            return "S"
        if shape == "P":
            return "R"
        if shape == "S":
            return "P"
    return shape


def parse_outcome_rounds(round_strs: List[str]) -> Tuple[str, str]:
    rounds = []
    for round_str in round_strs:
        plays = round_str.split()
        needed_shape = get_needed_shape(
            parse_shape(plays[0]),
            response_outcome[plays[1]]
        )
        rounds.append((parse_shape(plays[0]), needed_shape))
    return rounds


def part2(input: List[str]):
    rounds = parse_outcome_rounds(input)
    return sum(get_round_scores(rounds))


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read().splitlines()
    assert part2(test_input) == 12


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")
    assert result == 13484

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
    assert result == 13433
