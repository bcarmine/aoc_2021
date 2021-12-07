import fileinput
import numpy as np
import typing


class Board(object):
    board: [[]]
    checkers: [[]]
    unchecked_board_numbers: list

    def __init__(self, board_values):
        self.board = np.asmatrix(np.array(board_values))
        self.checkers = np.full(self.board.shape, False)
        self.unchecked_board_numbers = list(self.board.flat)

    def apply_drawn_number(self, number):
        location = np.where(self.board == number)
        if location:
            self.checkers[location] = True
            if number in self.unchecked_board_numbers:
                self.unchecked_board_numbers.remove(number)
            if self.has_won():
                return True

    def has_won(self):
        # check for all True rows or columns in the checkers matrix
        for checker_direction in [self.checkers, np.transpose(self.checkers)]:
            for direction in checker_direction:
                if np.all(direction == True):
                    return True
        return False

    def calculate_score(self, winning_number):
        # Sum the unchecked board numbers
        sum_unchecked_numbers = sum(int(number) for number in self.unchecked_board_numbers)
        print(f"Sum of unchecked numbers: {sum_unchecked_numbers}")
        return sum_unchecked_numbers * int(winning_number)


class Game(object):
    drawn_numbers: list
    boards: typing.List[Board] = None
    minimum_board_dimension: int

    def __init__(self, drawn_numbers, boards):
        self.drawn_numbers = drawn_numbers
        self.boards = [Board(board_values) for board_values in boards]
        # min board dim can be found from the lesser of the number of rows or columns in the boards
        self.minimum_board_dimension = min(self.boards[0].board.shape)

    def play(self):
        game_won, winner, numbers_drawn, winning_number = self.play_numbers()
        if game_won:
            print(f"Game won after {numbers_drawn} drawn numbers")
            print(f"Winning number: {winning_number}")
            score = winner.calculate_score(winning_number)
            print(f"Winning score: {score}")
        return

    def play_numbers(self):
        for index, number in enumerate(self.drawn_numbers):
            for board in self.boards:
                board_has_won = board.apply_drawn_number(number)
                if board_has_won:
                    return True, board, index, number
        return False, None, None

    def play_to_loose(self):
        winning_boards = []
        winning_bingo_numbers = []
        for index, number in enumerate(self.drawn_numbers):
            if len(winning_boards) == len(self.boards):
                break

            for board in self.boards:
                if board in winning_boards:  # skip boards that have already won
                    continue
                board_has_won = board.apply_drawn_number(number)
                if board_has_won:
                    winning_boards.append(board)
                    winning_bingo_numbers.append(number)

        # find the loosing board not included in the winning boards list
        loosing_board = winning_boards[-1]
        score = loosing_board.calculate_score(winning_bingo_numbers[-1])
        print(f"Loosing score: {score}")


# Part 1
print("\n---- Part 1 ----")
line_number = 0
drawn_numbers = []

board_values = []  # list, with one nested list per row
boards = []  # list of boards and their values

for line in fileinput.input():
    if line_number == 0:  # first line is the drawn numbers of the bingo game
        drawn_numbers = line.strip('\n').split(",")
    elif line == '\n' and board_values:  # new lines separate boards, add next board to boards
        boards.append(board_values)
        board_values = []
    elif line != '\n':  # add this row of numbers to the current board values
        board_row = [v for v in line.strip('\n').replace("  ", " ").split(" ") if v != '']
        board_values.append(board_row)
    line_number += 1
boards.append(board_values)

game = Game(drawn_numbers, boards)
game.play()

# Part 2
print("---- Part 2 ----")
loosing_game = Game(drawn_numbers, boards)
loosing_game.play_to_loose()