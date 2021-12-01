from helpers.utils import Utils


class Day__DAY__:
    def __init__(self, utils: Utils) -> None:
        self.utils = utils
        self.input_raw = self.utils.download_file()

    def run(self) -> None:
        self.utils.print_result(1, self.part1(), self.part2())

    def part1(self) -> int:
        return 1

    def part2(self) -> int:
        return 2
