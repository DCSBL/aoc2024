# ----------- IMPORTS ------------ #
from __future__ import annotations

import os


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


class Rule:
    before: int
    after: int

    def __init__(self, before: int, after: int):
        self.before = before
        self.after = after

    def honors(self, index: int, update: list[int] | None) -> bool:
        if update[index] is not self.before and update[index] is not self.after:
            return True

        start_section = update[0:index]
        end_section = update[index + 1:]

        if self.after in start_section:
            return False

        if self.before in end_section:
            return False

        return True


def check_update(update: list[int], rules: list[Rule]) -> bool:
    for idx, _ in enumerate(update[:-1]):
        for rule in rules:
            if not rule.honors(idx, update):
                return False

    return True


async def solution(filename: str) -> int:
    rules: list[Rule] = []
    updates: list[list[int]] = []

    with open(get_path(filename), mode="r") as file:
        for line in file.readlines():
            line = line.strip()

            if "|" in line:
                line = line.split("|")
                line = [int(x) for x in line]
                rules.append(Rule(line[0], line[1]))
            elif "," in line:
                line = line.split(",")
                line = [int(x) for x in line]
                updates.append(line)

    result = 0
    for update in updates:
        if check_update(update, rules):
            result += update[int((len(update) - 1) / 2)]

    return result
