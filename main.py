import argparse
from helpers.utils import Utils

from days.day1 import Day1

def check_day(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue > 25:
        raise argparse.ArgumentTypeError(f"{value} is an invalid day")
    return ivalue

def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2021")
    parser.add_argument("--day", type=check_day, required=True, help="The day to run")
    args = parser.parse_args()
    
    utils = Utils(args.day)
    
    match args.day:
        case 1:
            day1 = Day1(utils)
            day1.run()
        case _:
            print(f"Day {args.day} not yet implemented")

main()