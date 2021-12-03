import time

from helpers.utils import Utils


class Day4:
    def __init__(self, utils: Utils, regen: bool) -> None:
        self.utils = utils
        if regen:
            self.utils.download_file()
        self.input_raw = self.utils.read_file()

    def run(self) -> None:
        start = time.time()
        part1 = self.part1()
        part2 = self.part2()
        self.utils.print_result(4, part1, part2, (time.time() - start))

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
