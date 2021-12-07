import fileinput

gamma_rate_values = []
epsilon_rate_values = []


def find_most_and_least_frequent_values(col):
    col = [int(i) for i in col]
    if sum(col) >= (len(col) / 2):
        return '1', '0'
    return '0', '1'


def find_longest_prefix_match(rows, cols, use_high_frequency):
    matches = rows
    for index in range(len(cols)):
        # update the columns to only contain matches so far
        cols = list(zip(*matches))
        # get the most frequent value in this index
        most_freq, least_freq = find_most_and_least_frequent_values(cols[index])
        match_index_value = most_freq if use_high_frequency else least_freq
        # filter matches list for rows that have a match to the match index value in the correct index
        matches = list(filter(lambda v: v[index] == match_index_value, matches))
        if len(matches) == 1:
            return matches[0]


# Part 1
print("---- Part 1 ----")
rows = []
for line in fileinput.input():
    rows.append(line.replace("", " ").split())
columns = list(zip(*rows))  # Transform rows into cols

for col in columns:
    gamma_value, epsilon_value = find_most_and_least_frequent_values(col)
    gamma_rate_values.append(gamma_value)
    epsilon_rate_values.append(epsilon_value)

# Convert the binary values into decimal
gamma_rate = int("".join(gamma_rate_values), 2)
epsilon_rate = int("".join(epsilon_rate_values), 2)
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_rate * epsilon_rate}")


# Part 2
print("\n---- Part 2 ----")
# rejoin the row values
rows = ["".join(row) for row in rows]

binary_oxygen_generator_rating = find_longest_prefix_match(rows, columns, use_high_frequency=True)
binary_co2_scrubber_rating = find_longest_prefix_match(rows, columns, use_high_frequency=False)
oxygen_generator_rating = int(binary_oxygen_generator_rating, 2)
co2_scrubber_rating = int(binary_co2_scrubber_rating, 2)

print(f"Oxygen generator rating: {oxygen_generator_rating}")
print(f"CO2 scrubber rating: {co2_scrubber_rating}")
print(f"Life support rating: {oxygen_generator_rating * co2_scrubber_rating}")