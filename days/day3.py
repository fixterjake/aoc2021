import time

from helpers.utils import Utils


class Day3:
    def __init__(self, utils: Utils, regen: bool) -> None:
        self.utils = utils
        if regen:
            self.utils.download_file()
        self.input_raw = self.utils.read_file()

    def run(self) -> None:
        start = time.time()
        part1 = self.part1()
        part2 = self.part2()
        self.utils.print_result(2, part1, part2, (time.time() - start))

    def part1(self) -> int:
        gamma = ""
        epsilon = ""
        for i in range(len(self.input_raw[0]) - 1):
            zero = sum(entry[i] in entry for entry in self.input_raw if entry[i] == "0")
            one = sum(entry[i] in entry for entry in self.input_raw if entry[i] == "1")
            if zero > one:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
        gamma_decimal = int(gamma, 2)
        epsilon_decimal = int(epsilon, 2)
        return gamma_decimal * epsilon_decimal

    def part2(self) -> int:
        oxygen = 0
        co2 = 0
        input_ox = self.input_raw.copy()
        input_co2 = self.input_raw.copy()
        for i in range(len(self.input_raw[0])):
            i_ox = [x[i] for x in input_ox]
            i_co2 = [x[i] for x in input_co2]
            if i_ox.count("1") >= i_ox.count("0"):
                input_ox = [x for x in input_ox if x[i] == "1"]
            else:
                input_ox = [x for x in input_ox if x[i] == "0"]
            if i_co2.count("1") < i_co2.count("0"):
                input_co2 = [x for x in input_co2 if x[i] == "1"]
            else:
                input_co2 = [x for x in input_co2 if x[i] == "0"]
            if len(input_ox) == 1:
                print(input_ox)
                oxygen = int(input_ox[0], 2)
            if len(input_co2) == 1:
                print(input_co2)
                co2 = int(input_co2[0], 2)

        return oxygen * co2
