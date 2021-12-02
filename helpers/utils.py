import os
import urllib.error
import urllib.request
from typing import List


class Utils:
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

    def generate_day(self) -> int:
        try:
            with open("helpers/day_template.py") as f:
                template = f.read()
            with open(f"days/day{self.day}.py", "w") as f:
                f.write(template.replace("__DAY__", str(self.day)))
            return 1
        except Exception as e:
            print(e)
            return 0

    def download_file(self) -> None:
        try:
            if os.path.exists(f"days/inputs/day{self.day}.txt"):
                os.remove(f"days/inputs/day{self.day}.txt")
            with open(".env") as f:
                contents = f.read()
                url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
                req = urllib.request.Request(url, headers={"Cookie": contents.strip()})
                input = urllib.request.urlopen(req).read().decode()
                with open(f"days/inputs/day{self.day}.txt", "w") as f:
                    f.write(input)
        except Exception:
            print("File download failed")
            exit(1)

    def read_file(self) -> List[str]:
        try:
            with open(f"days/inputs/day{self.day}.txt") as f:
                return f.readlines()
        except Exception:
            print("File not found")
            exit(1)

    def print_result(
        self, day: int, result_one: str, result_two: int, time: float
    ) -> None:
        print(f"Day {day}")
        print(f"Part 1: {result_one}")
        print(f"Part 2: {result_two}")
        print(f"Time: {round(time, 5)}")

    def get_input_path(self, day: int) -> str:
        return f"days/inputs/day{day}.txt"
