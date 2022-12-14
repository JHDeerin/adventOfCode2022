"""
You need to delete files on a device to free up space. As input, we get a terminal log with commands being run (cd and ls) and then a list of files/directories. Commands are on lines starting with `$` (then either an `ls` or `cd` command; if `cd`, then there'll be the name of a directory). There are 3 possible commands: `cd /` (outermost directory), `cd x` (move down one level into folder X), `cd ..` (move up one level)

PART 1: Given a set of commands that traverses all files in a system, what is the total sum size of ALL directories that are AT MOST 100,000 in size? (double-counting files that are in nested directories IS allowed)
- Represent the file structure as a tree (nodes have a total size and link to sub-folders/files), then traverse it with DFS to get all the directory sizes - I think that's correct?
- Need to also travel up, so have nodes also link to their parents?
- This is a less-quick one, but doable just need to not panic (it's been forever since I've coded a tree)

OUTCOME: Took FOREVER, but got it right first try! (1844187)

PART 2: The total disk space of the device is 70000000 bytes; you need 30000000 of unused space. Get the size of the smallest directory that would free up enough space.
- Get the amount of free space we need (needed size - (max size - size of root))
- Get all directories, sorted by ascending size, and find the smallest one >= the size we need (could do a binary search, I'm just gonna iterate linearly)

OUTCOME: Got it right! (4978279)

REFLECTIONS:
- Okay, the first part took me FOREVER (like almost an hour), but then the 2nd part went pretty quick (<5 mniutes). A lot of it was me remembering how to make a tree; I also probably should've made some smaller unit tests (I was definitely nervous coding these larger parsing pieces without intermediate tests; I compensated via print-line debugging, and the nerves probably slowed me down more than the actual errors, but still)
- The regex took me a bit to remember; I had to look up a few things, and probably didn't need regex at all (splitting would've been totally sufficient).
- Couldn't remember how to code DFS exactly (knew it was appending nodes to a stack, but forgot how to avoid visiting previous nodes - although with a tree it should be a DAG anyway?), so I fell back to a flood fill (which for this problem is totally sufficient, but not great)
- I think my overall approach was fine, it just took me awhile to think through each individual piece.
- Looking at other solutions:
    -   betaveros: Solved this in just 5 minutes, holy cow (2 minutes faster than the runner up; the top 100 was barely within 15 minutes)
        -   He parsed the CLI input in by breaking on spaces, then just did a switch statement for each possible condition (e.g. `case ('$', 'cd', '/')`) - smart
        -   He assumed each directory would be ls'd exactly once, so he ignored ls commands, then kept the current working directory path as an array, and the file size for each dir in a dictionary. For `cd x` commands he'd append to the path, for `cd ..` commands he'd pop, and for files he'd iterate through all the subpaths of the CWD and add the size of each one to the dictionary.
        -   So, for the first part, he then just got all the size values in the dictionary, filtered, and summed
        -   For the 2nd part, he got the needed size, then filtered to get all he sizes under that, then got the `.min()` of the list
        -   So, yeah - smart use of constraints to speed up the problem
    -   oliver-ni: actually scarily similar to betaveros's solution
        -   The 1st part solution is literally identical, just in Python (and he used the `Path` class instead of an array) - and, I guess, he only cared about 2 cases (because of the Path class, was able to handle the `cd ..` command for free)
        -   For the 2nd part, also did the same thing - filtered, then took the min (I guess that is simpler to fit into headspace than sorting and searching; neat)
"""
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class File:

    name: str
    parent: Optional["File"] = None
    children: Dict[str, "File"] = field(default_factory=dict)
    size: int = 0

    def is_dir(self) -> bool:
        return bool(self.children)

    def add_file(self, file: "File"):
        file.parent = self
        self.children[file.name] = file
        self.update_size(self, file.size)

    @classmethod
    def update_size(cls, current_dir: Optional["File"], change_size: int):
        if current_dir is None:
            return
        current_dir.size += change_size
        cls.update_size(current_dir.parent, change_size)

    @classmethod
    def get_root(cls, current_dir: "File"):
        if current_dir.parent is None:
            return current_dir
        return cls.get_root(current_dir.parent)

    @classmethod
    def get_directories(cls, root: "File") -> List["File"]:
        # Get directories via BFS
        dirs = []
        if root.is_dir():
            dirs.append(root)
        for _, file in root.children.items():
            dirs += cls.get_directories(file)
        return dirs


def apply_command(line: str, current_dir: Optional[File]) -> File:
    command_match: Optional[re.Match] = re.match(r"\$ (cd|ls)\s?(.+)?", line)
    command = command_match.group(1)
    assert command in ["cd", "ls"]
    if command == "ls":
        return current_dir
    new_dir_name = command_match.group(2)
    if new_dir_name == ".." and current_dir:
        return current_dir.parent
    if new_dir_name == "/" and current_dir:
        return File.get_root(current_dir)
    if not current_dir:
        return File(name=new_dir_name)
    return current_dir.children[new_dir_name]


def make_file(line: str) -> File:
    file_match: Optional[re.Match] = re.match(r"(.+) (.+)", line)
    size, name = file_match.group(1), file_match.group(2)
    if size.isnumeric():
        return File(name=name, size=int(size))
    return File(name=name, size=0)


def get_file_structure(input: List[str]) -> File:
    current_dir = None
    for line in input:
        is_command = line[0] == "$"
        if is_command:
            current_dir = apply_command(line, current_dir)
        elif current_dir:
            current_dir.add_file(make_file(line))
    current_dir = File.get_root(current_dir)
    return current_dir


def part1(input: str) -> int:
    root_directory = get_file_structure(input.splitlines())
    directories = File.get_directories(root_directory)
    return sum(dir.size for dir in directories if dir.size <= 100000)


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part1(test_input) == 95437


def part2(input: str):
    root_directory = get_file_structure(input.splitlines())
    directories = File.get_directories(root_directory)
    total_space, required_space = 70000000, 30000000
    space_available = total_space - root_directory.size
    space_needed = (required_space - space_available)
    for dir in sorted(directories, key=lambda x: x.size):
        if dir.size >= space_needed:
            return dir.size
    raise ValueError("No directory big enough to delete")


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 24933642


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")
    assert result == 1844187

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
    assert result == 4978279
