import fileinput

horizontal_movement = 0
depth = 0


def process_forward(value: int):
    global horizontal_movement
    horizontal_movement += value


def process_up(value: int):
    global depth
    depth -= value


def process_down(value: int):
    global depth
    depth += value


def process_line(line: str):
    direction, value = line.split(" ")
    eval(f"process_{direction}({value})")


for line in fileinput.input():
    if line:
        process_line(line)

print(f"Horizontal movement: {horizontal_movement}")
print(f"Depth: {depth}")

print(f"\nhorizontal_movement * depth = {horizontal_movement*depth}")

