# ----------- IMPORTS ------------ #
import copy
import os
from enum import Enum


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    safe_reports: int = 0

    def in_order(report: list[int]) -> bool:
        class Direction(Enum):
            Unknown = -1
            ASC = 0
            DEC = 1

        prev: int | None = None
        direction: Direction = Direction.Unknown

        for idx, level in enumerate(report):
            if prev is not None:
                if prev <= level and direction in (Direction.Unknown, Direction.ASC):
                    direction = Direction.ASC

                elif prev >= level and direction in (Direction.Unknown, Direction.DEC):
                    direction = Direction.DEC

                else:
                    raise ValueError(f"not in order - {report}")

            prev = level

    def differ_at_least_1_most_3(report: list[int]) -> bool:
        prev: int | None = None

        for idx, level in enumerate(report):
            if prev is not None and not 1 <= abs(prev - level) <= 3:
                raise ValueError(f"not in range - {report}")

            prev = level

    with open(get_path(filename), mode="r") as file:
        for report in file.readlines():
            report = report.split(" ")
            for idx, level in enumerate(report):
                report[idx] = int(level)

            try:
                in_order(report)
                differ_at_least_1_most_3(report)
                safe_reports += 1
                continue
            except ValueError:
                for i in range(len(report)):
                    report_copy = copy.deepcopy(report)
                    del report_copy[i]

                    try:
                        in_order(report_copy)
                        differ_at_least_1_most_3(report_copy)
                        safe_reports += 1
                        break
                    except ValueError as e2:
                        print("Still not ok", e2)
                        continue

    return safe_reports
