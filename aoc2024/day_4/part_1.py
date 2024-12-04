# ----------- IMPORTS ------------ #
import os


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #

# fmt: off
HORIZONTAL_MATRICES = [
    [
        ['X', 'M', 'A', 'S'],
    ],
    [
        ['S', 'A', 'M', 'X'],
    ],
]

VERTICAL_MATRICES = [
    [
        ['X'],
        ['M'],
        ['A'],
        ['S'],
    ],
    [
        ['S'],
        ['A'],
        ['M'],
        ['X'],
    ],
]

DIAGONAL_MATRICES = [
    [
        ['X', ' ', ' ', ' '],
        [' ', 'M', ' ', ' '],
        [' ', ' ', 'A', ' '],
        [' ', ' ', ' ', 'S'],
    ],
    [
        ['S', ' ', ' ', ' '],
        [' ', 'A', ' ', ' '],
        [' ', ' ', 'M', ' '],
        [' ', ' ', ' ', 'X'],
    ],
    [
        [' ', ' ', ' ', 'X'],
        [' ', ' ', 'M', ' '],
        [' ', 'A', ' ', ' '],
        ['S', ' ', ' ', ' '],
    ],
    [
        [' ', ' ', ' ', 'S'],
        [' ', ' ', 'A', ' '],
        [' ', 'M', ' ', ' '],
        ['X', ' ', ' ', ' '],
    ],
]
# fmt: on


def match(grid, at_x, at_y, matrix, m_width, m_height) -> bool:
    for mx in range(m_width):
        for my in range(m_height):
            if matrix[my][mx] == " ":
                continue

            if grid[at_y + my][at_x + mx] != matrix[my][mx]:
                return False

    return True


def find(grid, width, height, matrices) -> int:
    count: int = 0

    for matrix in matrices:
        m_width = len(matrix[0])
        m_height = len(matrix)

        for x in range(0, (width - m_width) + 1):
            for y in range(0, (height - m_height) + 1):
                if match(grid, x, y, matrix, m_width, m_height):
                    count += 1

    return count


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

    hor = find(grid, width, height, HORIZONTAL_MATRICES)
    ver = find(grid, width, height, VERTICAL_MATRICES)
    dia = find(grid, width, height, DIAGONAL_MATRICES)

    return hor + ver + dia
