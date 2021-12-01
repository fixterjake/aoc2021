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
    parser.add_argument("--gen", action="store_true", help="Generate day")
    parser.add_argument("--regen", action="store_true", help="Redownload input")
    args = parser.parse_args()

    utils = Utils(2021, args.day)

    if args.gen:
        utils.generate_day()
        return

    if args.day == 1:
        day_one = Day1(utils, args.regen)
        day_one.run()
    else:
        print(f"Day {args.day} not yet implemented")


main()
