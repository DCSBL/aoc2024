# ----------- IMPORTS ------------ #
from __future__ import annotations

import os

from .part_1 import Rule, check_update


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


def fix_update(update: list[int], rules: list[Rule]) -> list[int]:
    rule_broken = False
    for idx, _ in enumerate(update):
        for rule in rules:
            if not rule.honors(idx, update):
                rule_broken = True
                index_after = update.index(rule.before)
                index_before = update.index(rule.after)

                update[index_before], update[index_after] = (
                    update[index_after],
                    update[index_before],
                )

    if rule_broken:
        return fix_update(update, rules)

    return update


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
        if not check_update(update, rules):
            update = fix_update(update, rules)
            result += update[int((len(update) - 1) / 2)]

    return result
