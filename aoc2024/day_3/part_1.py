# ----------- IMPORTS ------------ #
import os
import re


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    currupt_program: str = ""

    with open(get_path(filename), mode="r") as file:
        for line in file.readlines():
            currupt_program += line.strip()

    result: int = 0

    functions = re.findall(r"mul\(\d+,\d+\)", currupt_program)
    for function in functions:
        match = re.match(r"mul\((\d+),(\d+)\)", function)

        result += int(match.group(1)) * int(match.group(2))

    return result
