import argparse

from days.day1 import Day1
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from helpers.utils import Utils


def check_day(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0 or ivalue > 25:
        raise argparse.ArgumentTypeError(f"{value} is an invalid day")
    return ivalue


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2021")
    parser.add_argument("--day", type=check_day, required=True, help="The day to run")
    parser.add_argument("--gen", action="store_true", help="Generate day")
    parser.add_argument("--download", action="store_true", help="Download input on run")
    args = parser.parse_args()

    utils = Utils(2021, args.day)

    if args.gen:
        utils.generate_day()
        return

    if args.day == 1:
        day_one = Day1(utils, args.download)
        day_one.run()
    elif args.day == 2:
        day_two = Day2(utils, args.download)
        day_two.run()
    elif args.day == 3:
        day_three = Day3(utils, args.download)
        day_three.run()
    elif args.day == 4:
        day_four = Day4(utils, args.download)
        day_four.run()
    else:
        print(f"Day {args.day} not yet implemented")


main()
