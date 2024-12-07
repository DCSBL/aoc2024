# ----------- IMPORTS ------------ #
import os
from copy import deepcopy

from .part_1 import Position, Type, move_guard, print_map


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


def generate_trail(
    guard_starting_position: Position, map: list[list[Type]]
) -> list[list[Type]]:
    _map = deepcopy(map)
    while True:
        guard_starting_position = move_guard(guard_starting_position, _map)
        if guard_starting_position is None:
            break

    return _map


def loop_detector(
    map: list[list[Type]], guard: Position, obstruction_pos: Position
) -> bool:
    _map = deepcopy(map)

    # Do not allow obstruction at guards location
    if guard == obstruction_pos:
        print("Guard in the way")
        return False

    # Place obstruction
    _map[obstruction_pos.y][obstruction_pos.x] = Type.Obstruction

    path = []

    while True:
        guard = move_guard(guard, _map)
        if guard is None:
            return False

        pos_dir = [guard, _map[guard.y][guard.x]]

        if pos_dir in path:
            return True

        path.append(pos_dir)


async def solution(filename: str) -> int:
    map: list[list[Type]] = []
    guard_starting_pos: Position = Position()

    with open(get_path(filename), mode="r") as file:
        for line in file.readlines():
            row = list(line.strip())
            row = [Type(x) for x in row]
            map.append(row)
            if Type.GuardUp in row:
                guard_starting_pos = Position(row.index(Type.GuardUp), len(map) - 1)

    print(guard_starting_pos)
    print_map(map)

    # Get potential path of guard
    trail = generate_trail(guard_starting_pos, map)
    print_map(trail)

    # Detect loop at every location the guard goes
    result = 0
    item = 0
    for idy, row in enumerate(trail):
        for idx, tile in enumerate(row):
            if tile in (
                Type.Footstep,
                Type.GuardUp,
                Type.GuardRight,
                Type.GuardDown,
                Type.GuardLeft,
            ):
                print(f"{item} out of 4964")
                item += 1
                if loop_detector(map, guard_starting_pos, Position(idx, idy)):
                    print("found loop")
                    result += 1

    return result
