# ----------- IMPORTS ------------ #
import os

from .part_1 import find


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #

# fmt: off
XMAS_MATRICES = [
    [
        ['M', ' ', 'S'],
        [' ', 'A', ' '],
        ['M', ' ', 'S'],
    ],
    [
        ['M', ' ', 'M'],
        [' ', 'A', ' '],
        ['S', ' ', 'S'],
    ],
    [
        ['S', ' ', 'M'],
        [' ', 'A', ' '],
        ['S', ' ', 'M'],
    ],
    [
        ['S', ' ', 'S'],
        [' ', 'A', ' '],
        ['M', ' ', 'M'],
    ],
]
# fmt: on


async def solution(filename: str) -> int:
    grid: list[list[int]] = []
    width: int = 0
    height: int = 0

    with open(get_path(filename), mode="r") as file:
        lines = file.readlines()

    width = len(lines[0].strip())
    height = len(lines)

    for line in lines:
        grid.append(list(line.strip()))

    xmas = find(grid, width, height, XMAS_MATRICES)

    return xmas
