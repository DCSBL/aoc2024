# ----------- IMPORTS ------------ #
import os


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    list_left: list[int] = []
    list_right: list[int] = []

    with open(get_path(filename), mode="r") as file:
        for line in file.readlines():
            line = line.split("   ")
            list_left.append(int(line[0]))
            list_right.append(int(line[1]))

    list_left.sort()
    list_right.sort()

    distance: int = 0

    for idx, x in enumerate(list_left):
        distance += abs(list_left[idx] - list_right[idx])

    return distance
