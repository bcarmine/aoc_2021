import fileinput
import numpy as np

diagram = None


def draw_horizontal_line(x1, x2, y):
    global diagram
    for x in range(min(x1, x2), max(x1, x2)+1):  # inclusive of x end
        diagram[y, x] += 1


def draw_vertical_line(y1, y2, x):
    global diagram
    for y in range(min(y1, y2), max(y1, y2)+1):  # inclusive of y end
        diagram[y, x] += 1


def draw_diagonal_line(x1, x2, y1, y2):
    global diagram
    x_step = -1 if x1 > x2 else 1
    y_step = -1 if y1 > y2 else 1

    x_range = range(x1, x2+x_step, x_step)
    y_range = range(y1, y2+y_step, y_step)

    for x, y in zip(x_range, y_range):
        diagram[y, x] += 1

# read in the coordinates as a list of lines, each line with two x and y coords
lines = []
for line in fileinput.input():
     lines.append([int(value) for value in line.strip().replace(" -> ", ",").split(",")])

x_dimension = int(max([max(line[0], line[2]) for line in lines]))
y_dimension = int(max([max(line[1], line[3]) for line in lines]))
# fill the diagram with 0 before we start drawing lines
diagram = np.full((x_dimension+1, y_dimension+1), 0)

# process the lines and alter the diagram
for line in lines:
    x1, y1, x2, y2 = line
    x_diff = abs(x1-x2)
    y_diff = abs(y1-y2)
    if x_diff and y_diff:
        draw_diagonal_line(x1, x2, y1, y2)
        continue
    if x_diff:
        draw_horizontal_line(x1, x2, y1)
    elif y_diff:
        draw_vertical_line(y1, y2, x1)


# count number of points in diagram >= 2
overlap_locations = np.where(diagram >= 2)
num_overlaps = len(overlap_locations[0])
print(f"Number of points where at least 2 lines overlap: {num_overlaps}")
print("\nDiagram:")
print(diagram)
