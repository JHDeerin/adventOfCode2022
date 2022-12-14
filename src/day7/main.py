"""
You need to delete files on a device to free up space. As input, we get a terminal log with commands being run (cd and ls) and then a list of files/directories. Commands are on lines starting with `$` (then either an `ls` or `cd` command; if `cd`, then there'll be the name of a directory). There are 3 possible commands: `cd /` (outermost directory), `cd x` (move down one level into folder X), `cd ..` (move up one level)

PART 1: Given a set of commands that traverses all files in a system, what is the total sum size of ALL directories that are AT MOST 100,000 in size? (double-counting files that are in nested directories IS allowed)
- Represent the file structure as a tree (nodes have a total size and link to sub-folders/files), then traverse it with DFS to get all the directory sizes - I think that's correct?
- Need to also travel up, so have nodes also link to their parents?
- This is a less-quick one, but doable just need to not panic (it's been forever since I've coded a tree)

OUTCOME: TODO

PART 2: TODO

OUTCOME: TODO

REFLECTIONS: TODO
"""
import re
from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass
class File:

    name: str
    parent: "File" = None
    children: Dict[str, "File"] = field(default_factory=dict)
    size: int = 0

    def is_dir(self) -> bool:
        return self.children

    def add_file(self, file: "File"):
        file.parent = self
        self.children[file.name] = file
        self.update_size(self, file.size)

    @classmethod
    def update_size(cls, current_dir: "File", change_size: int):
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


def apply_command(line: str, current_dir: File) -> File:
    command_match: re.Match = re.match(r"\$ (cd|ls)\s?(.+)?", line)
    command = command_match.group(1)
    assert command in ["cd", "ls"]
    if command == "ls":
        return current_dir
    new_dir_name = command_match.group(2)
    if new_dir_name == ".." and current_dir:
        return current_dir.parent
    if new_dir_name == "/" and current_dir:
        return current_dir.parent
    if not current_dir:
        return File(name=new_dir_name)
    return current_dir.children[new_dir_name]


def make_file(line: str) -> File:
    file_match: re.Match = re.match(r"(.+) (.+)", line)
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
        else:
            current_dir.add_file(make_file(line))
    current_dir = File.get_root(current_dir)
    return current_dir


def part1(input: str) -> int:
    root_directory = get_file_structure(input.splitlines())
    directories = File.get_directories(root_directory)
    print([f"{dir.name}: {dir.size}" for dir in directories])
    return sum(dir.size for dir in directories if dir.size <= 100000)


def test_first_example():
    with open("test.txt") as file:
        test_input = file.read()
    print(part1(test_input))
    assert part1(test_input) == 95437


def part2(input: str):
    pass


def test_second_example():
    with open("test.txt") as file:
        test_input = file.read()
    assert part2(test_input) == 0


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    test_first_example()
    result = part1(input)
    print(f"part 1: {result}")

    test_second_example()
    result = part2(input)
    print(f"part 2: {result}")
