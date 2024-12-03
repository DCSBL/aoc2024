# ----------- IMPORTS ------------ #
import os


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    with open(get_path(filename), mode="r") as file:
        del file
        pass

    return 0
