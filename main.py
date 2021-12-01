import argparse
from helpers.utils import Utils

from days.day1 import Day1


def check_day(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue > 25:
        raise argparse.ArgumentTypeError(f"{value} is an invalid day")
    return ivalue


def check_year(value):
    ivalue = int(value)
    if ivalue != 2020:
        raise argparse.ArgumentTypeError(f"{value} is an invalid year")
    return ivalue


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2021")
    parser.add_argument(
        "--year", type=check_year, required=True, help="The year to run"
    )
    parser.add_argument("--day", type=check_day, required=True, help="The day to run")
    parser.add_argument("--gen", action="store_true", help="Generate day")
    parser.add_argument("--input", action="store_true", help="Download input")
    args = parser.parse_args()

    utils = Utils(args.year, args.day)

    if args.gen:
        utils.generate_day()
        return

    if args.input:
        utils.download_input()
        return

    if args.day == 1:
        day_one = Day1(utils)
        day_one.run()
    else:
        print(f"Day {args.day} not yet implemented")


main()
