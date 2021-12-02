import csv
import typing
import functools


def cumulative_increase_counter(a: typing.Tuple[int, int], b: int) -> typing.Tuple[int, int]:
    count, last_digit = a
    if b > last_digit:
        count += 1
    return count, b


if __name__ == "__main__":
    with open("aoc2021_1.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        measurements = []
        for row in reader:
            for header, value in row.items():
                if value:
                    measurements.append(int(value))
                    
        cumulative_increase_count, last_value = functools.reduce(cumulative_increase_counter, measurements, (0, max(measurements)))
        print(f"Total increased measurements: {cumulative_increase_count} from {len(measurements)} measurements")


