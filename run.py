import argparse
import asyncio
import importlib
import time


def validate_part(value) -> int:
    ivalue = int(value)
    if ivalue not in (1, 2):
        raise argparse.ArgumentTypeError(f"Part must be 1 or 2, got {value}")
    return ivalue


parser = argparse.ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("part", type=validate_part)
parser.add_argument("--real", action="store_true")
args = parser.parse_args()

# Dynamically import the specified part as a submodule
try:
    solution_function = importlib.import_module(
        f"aoc2024.day_{args.day}.part_{args.part}"
    )
except ModuleNotFoundError as e:
    print(f"Error: Could not find module for day {args.day}, part {args.part}.")
    print(e)
    exit(1)

filename = "input.txt" if args.real else "example.txt"
print(f"Using {filename}")

event_loop = asyncio.new_event_loop()
start_time = time.time()
print(
    f"=== Solution: {event_loop.run_until_complete(solution_function.solution(filename))} ==="
)
print(f"{(time.time() - start_time)} seconds")
