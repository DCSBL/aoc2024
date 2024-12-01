# ----- IMPORTS AND HELPERS ------ #
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

    def count_num_of(value: int) -> int:
        return len(list(filter(lambda x: x == value, list_right)))

    similarity_score: int = 0

    for id in list_left:
        similarity_score += id * count_num_of(id)

    return similarity_score
