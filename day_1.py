import csv
import typing
import functools


def cumulative_increase_counter(a: typing.Tuple[int, int], b: int) -> typing.Tuple[int, int]:
    count, last_digit = a
    if b > last_digit:
        count += 1
    return count, b


if __name__ == "__main__":
    with open("data/day_1.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        measurements = []
        for row in reader:
            for header, value in row.items():
                if value:
                    measurements.append(int(value))

        # Part 1:
        print("---- Part 1 ----")
        cumulative_increase_count, last_value = functools.reduce(cumulative_increase_counter, measurements, (0, max(measurements)))
        print(f"Total increased measurements: {cumulative_increase_count} from {len(measurements)} measurements")

        # Part 2
        window_measurements = []
        for i, m in enumerate(measurements):
            try:
                window_measurements.append(sum([m, measurements[i+1], measurements[i+2]]))
            except IndexError:
                continue

        print("\n---- Part 2 ----")
        cumulative_increase_count, last_value = functools.reduce(cumulative_increase_counter, window_measurements, (0, max(window_measurements)))
        print(f"Total increased measurements: {cumulative_increase_count} from {len(window_measurements)} window measurements")




