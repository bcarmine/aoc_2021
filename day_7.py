import fileinput


def triangular_number(a, b):
    n = abs(a-b)
    return (n * (n+1)) / 2.0


def calc_fuel_position_per_pos(is_crab_engineering_understood, positions):
    fuel_consumption_per_pos = []
    for potential_pos in range(min_position, max_position + 1):
        if is_crab_engineering_understood:
            fuel_consumption_per_pos.append(sum([triangular_number(potential_pos, p) for p in positions]))
        else:
            fuel_consumption_per_pos.append(sum([abs(potential_pos - p) for p in positions]))

    return fuel_consumption_per_pos


positions = []
for line in fileinput.input():
    positions = [int(value) for value in line.split(",")]

min_position = min(positions)
max_position = max(positions)

for crab_engineering_understood_value in [False, True]:
    if crab_engineering_understood_value:
        print("\nCrab engineering is understood !!!")
    else:
        print("Crab engineering is not understood ...")

    fuel_consumption_per_pos = calc_fuel_position_per_pos(crab_engineering_understood_value, positions)
    # get the minimum fuel consumption from all tested positions
    min_fuel_consumption = min(fuel_consumption_per_pos)
    print(f"Minimum fuel consumption: {min_fuel_consumption}")
    # get the position of the minimum fuel consumption
    min_fuel_consumption_pos = fuel_consumption_per_pos.index(min_fuel_consumption)
    print(f"Position of minimum fuel consumption: {min_fuel_consumption_pos}")
