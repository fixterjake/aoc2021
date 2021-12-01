from helpers.utils import Utils


class Day1:
    def __init__(self, utils: Utils, regen: bool) -> None:
        self.utils = utils
        if regen:
            self.utils.download_file()
        self.input_raw = self.utils.read_file()

    def run(self) -> None:
        self.utils.print_result(1, self.part1(), self.part2())

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
