from typing import List


class Utils:
    def __init__(self, day: int):
        self.day = day

    def read_file(self, path: str) -> List[str]:
        with open(path) as f:
            return f.readlines()

    def print_result(self, day: int, result: str) -> None:
        print(f"Day {day} result: {result}")

    def get_input_path(self, day: int) -> str:
        return f"inputs/day{day}.txt"

    def try_parse_int(self, value: str) -> int:
        try:
            return int(value)
        except ValueError:
            return 0

    def try_parse_float(self, value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0
