import time
from helpers.utils import Utils


class Day2:
    def __init__(self, utils: Utils, regen: bool) -> None:
        self.utils = utils
        if regen:
            self.utils.download_file()
        self.input_raw = self.utils.read_file()
        self.depth_a = 0
        self.position_a = 0

        self.depth_b = 0
        self.position_b = 0
        self.aim_b = 0

    def run(self) -> None:
        start = time.time()
        part1 = self.part1()
        part2 = self.part2()
        self.utils.print_result(2, part1, part2, (time.time() - start))

    def part1(self) -> int:
        for entry in self.input_raw:
            entry_list = entry.split(" ")
            if entry_list[0] == "forward":
                self.position_a += int(entry_list[1])
            if entry_list[0] == "up":
                self.depth_a -= int(entry_list[1])
            if entry_list[0] == "down":
                self.depth_a += int(entry_list[1])
        return self.position_a * self.depth_a

    def part2(self) -> int:
        for entry in self.input_raw:
            entry_list = entry.split(" ")
            if entry_list[0] == "forward":
                self.position_b += int(entry_list[1])
                self.depth_b += self.aim_b * int(entry_list[1])
            elif entry_list[0] == "up":
                self.aim_b -= int(entry_list[1])
            elif entry_list[0] == "down":
                self.aim_b += int(entry_list[1])
        return self.position_b * self.depth_b
