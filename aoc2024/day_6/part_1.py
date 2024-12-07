# ----------- IMPORTS ------------ #
import os
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


class Type(Enum):
    Floor = "."
    GuardUp = "^"
    GuardLeft = "<"
    GuardRight = ">"
    GuardDown = "v"
    Item = "#"
    Footstep = "X"
    Obstruction = "O"


@dataclass
class Position:
    x: int = 0
    y: int = 0


@dataclass
class Step:
    dir: Type
    position: Position


def print_map(map: list[list[Type]]):
    for row in map:
        for tile in row:
            print(tile.value, end="")
        print()

    print("=" * len(map[0]))


def get_next_pos(type: Type, pos: Position) -> Position:
    new_pos = deepcopy(pos)

    if type == Type.GuardUp:
        new_pos.y -= 1

    if type == Type.GuardRight:
        new_pos.x += 1

    if type == Type.GuardDown:
        new_pos.y += 1

    if type == Type.GuardLeft:
        new_pos.x -= 1

    return new_pos


def get_next_rotation(type: Type) -> Type:
    if type == Type.GuardUp:
        return Type.GuardRight

    if type == Type.GuardRight:
        return Type.GuardDown

    if type == Type.GuardDown:
        return Type.GuardLeft

    if type == Type.GuardLeft:
        return Type.GuardUp


def move_guard(pos: Position, map: list[list[Type]]) -> Position:
    guard = map[pos.y][pos.x]
    next_pos = get_next_pos(guard, pos)

    if next_pos.y < 0 or next_pos.y >= len(map):
        return None

    if next_pos.x < 0 or next_pos.x >= len(map[0]):
        return None

    if map[next_pos.y][next_pos.x] in (Type.Item, Type.Obstruction):
        map[pos.y][pos.x] = get_next_rotation(guard)
        return pos

    if map[next_pos.y][next_pos.x] in (Type.Floor, Type.Footstep):
        map[pos.y][pos.x] = Type.Footstep
        pos = next_pos
        map[pos.y][pos.x] = guard
        return next_pos


async def solution(filename: str) -> int:
    map: list[list[Type]] = []
    pos: list[int, int] = Position

    with open(get_path(filename), mode="r") as file:
        for line in file.readlines():
            row = list(line.strip())
            row = [Type(x) for x in row]
            map.append(row)
            if Type.GuardUp in row:
                pos = Position(row.index(Type.GuardUp), len(map) - 1)

    print(pos)
    print_map(map)

    while True:
        pos = move_guard(pos, map)
        if pos is None:
            break

    print_map(map)

    result = 0
    for row in map:
        for tile in row:
            if tile in (
                Type.Footstep,
                Type.GuardUp,
                Type.GuardRight,
                Type.GuardDown,
                Type.GuardLeft,
            ):
                result += 1

    return result
