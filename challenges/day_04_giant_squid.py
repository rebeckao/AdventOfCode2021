from typing import List, Set, Tuple


def winning_score(numbers: List[int], raw_boards: List[str]) -> int:
    board_side_length = len(raw_boards[0].split())
    boards = _to_boards(raw_boards, board_side_length)
    for number in numbers:
        for board in boards:
            for idx, row in enumerate(board.all_rows):
                if number in row:
                    board.row_completion[idx] += 1
                    if number in board.unmarked_numbers:
                        board.unmarked_numbers.remove(number)
                    if board.row_completion[idx] >= board_side_length:
                        sum_of_unmarked_numbers = sum(board.unmarked_numbers)
                        return sum_of_unmarked_numbers * number
    return 0


def losing_score(numbers: List[int], raw_boards: List[str]) -> int:
    board_side_length = len(raw_boards[0].split())
    boards = _to_boards(raw_boards, board_side_length)
    most_numbers_until_win = 0
    loser_score = []
    for board in boards:
        numbers_until_win, score = _play_until_win(board_side_length, board, numbers)
        if numbers_until_win > most_numbers_until_win:
            most_numbers_until_win = numbers_until_win
            loser_score = score
    return loser_score


def _play_until_win(board_side_length, board, numbers) -> Tuple[int, int]:
    for number_idx, number in enumerate(numbers):
        for idx, row in enumerate(board.all_rows):
            if number in row:
                board.row_completion[idx] += 1
                if number in board.unmarked_numbers:
                    board.unmarked_numbers.remove(number)
                if board.row_completion[idx] >= board_side_length:
                    sum_of_unmarked_numbers = sum(board.unmarked_numbers)
                    return number_idx, sum_of_unmarked_numbers * number


def _to_boards(raw_boards, board_side_length):
    boards: List[Board] = []
    board_index = 0
    row_in_board = 0
    current_board = Board(board_side_length)
    for line in raw_boards:
        if line == "":
            board_index += 1
            row_in_board = 0
            boards.append(current_board)
            current_board = Board(board_side_length)
            continue
        row_values = [int(value) for value in line.split()]
        current_board.rows.append(row_values)
        for idx, value in enumerate(row_values):
            current_board.columns[idx].append(value)
        row_in_board += 1
    boards.append(current_board)
    for board in boards:
        board.finalize()
    return boards


class Board:
    rows: List[List[int]]
    columns: List[List[int]]
    all_rows: List[List[int]]
    row_completion: List[int]
    unmarked_numbers: Set[int]

    def __init__(self, board_side_length: int):
        self.rows = []
        self.columns = [[] for i in range(board_side_length)]

    def finalize(self):
        self.all_rows = self.rows + self.columns
        self.row_completion = [0 for _ in self.all_rows]
        self.unmarked_numbers = set()
        for row in self.all_rows:
            for value in row:
                self.unmarked_numbers.add(value)
