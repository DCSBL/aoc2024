import argparse
import asyncio
import os
import time

# ----------- SOLUTION ----------- #


async def solution(file: str) -> int:
    list_left = []
    list_right = []

    with open(FILE, mode="r") as file:
        for line in file.readlines():
            line = line.split("   ")
            list_left.append(int(line[0]))
            list_right.append(int(line[1]))

    def count_num_of(value: int) -> int:
        return len(list(filter(lambda x: x == value, list_right)))

    similarity_score = 0

    for id in list_left:
        similarity_score += id * count_num_of(id)

    return similarity_score


# ---------- BOILERPLATE --------- #
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", action="store_true")
    args = parser.parse_args()

    filename = "input.txt" if args.real else "example.txt"
    print(f"Using {filename}")

    # Get absolute location so we can run from root
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    FILE = os.path.join(__location__, filename)

    event_loop = asyncio.new_event_loop()
    start_time = time.time()
    print(f"=== Solution: {event_loop.run_until_complete(solution(FILE))} ===")
    print(f"{(time.time() - start_time)} seconds")
