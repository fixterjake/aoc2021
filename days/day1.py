from helpers.utils import Utils


class Day1:
    def __init__(self, utils: Utils, regen: bool) -> None:
        self.utils = utils
        if regen:
            self.utils.download_file()
        self.input_raw = self.utils.read_file()

    def run(self) -> None:
        self.parse_input()
        self.utils.print_result(1, self.part1(), self.part2())

    def parse_input(self) -> None:
        self.input = list()
        for entry in self.input_raw:
            self.input.append(int(entry))

    def part1(self) -> int:
        increase = 0
        for i in range(1, len(self.input)):
            if self.input[i] > self.input[i - 1]:
                increase += 1
        return increase

    def part2(self) -> int:
        increase = 0
        for i in range(3, len(self.input)):
            if self.input[i] > self.input[i - 3]:
                increase += 1
        return increase
