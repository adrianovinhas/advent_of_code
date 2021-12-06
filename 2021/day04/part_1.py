from itertools import dropwhile
import sys
from typing import Optional

Board = list[list[int]]
ScratchedBoard = list[list[bool]]


def find_number(number: int, board: Board) -> Optional[tuple[int,int]]:
    for i in range(len(board)):
        if number in board[i]:
            return i, board[i].index(number)
    return None


def is_winner_found(number,
                    board: Board,
                    board_flags: list[ScratchedBoard],
                    board_flags_transposed: list[ScratchedBoard]) -> bool:
   
        found_position: tuple[int,int] = find_number(number, board)
        if found_position is not None:
            board_flags[found_position[0]][found_position[1]] = True
            board_flags_transposed[found_position[1]][found_position[0]] = True
            if sum(board_flags[found_position[0]]) == 5 or \
                sum(board_flags_transposed[found_position[1]]) == 5:
                return True
        return False


numbers_drawn_total: list[int] = list(map(int, sys.stdin.readline()[:-1].split(",")))
boards_input_str: list[list[str]] = list(map(lambda x: " ".join(x.split()).split(), sys.stdin.readlines()))
boards_input: list[list[int]] = list(map(lambda x: list(map(int, x)), boards_input_str))

assert len(boards_input) % 6 == 0

boards_list: list[Board] = [boards_input[i+1:i+6] for i in range(0, len(boards_input), 6)]
boards_flags: list[ScratchedBoard] = [[[False for i in range(5)] for i in range(5)] for i in range(len(boards_input))]
boards_flags_transposed: list[ScratchedBoard] = [[[False for i in range(5)] for i in range(5)] for i in range(len(boards_input))]

numbers_not_drawn_per_board: list[list[int]] = \
    [list(dropwhile(lambda n: is_winner_found(n, board, board_flags, board_flags_transposed) is False,
                    numbers_drawn_total))
     for board, board_flags, board_flags_transposed in \
         zip(boards_list, boards_flags, boards_flags_transposed)]

counts_numbers_not_drawn: list[int] = list(map(lambda x: len(x[1:]), numbers_not_drawn_per_board))
most_numbers_not_drawn: int = max(counts_numbers_not_drawn)
 
winner_board_index: int = counts_numbers_not_drawn.index(most_numbers_not_drawn)
flatten_winner_board = sum(boards_list[winner_board_index], [])

sum_not_drawn_numbers = sum(
    list(filter(lambda x: x in flatten_winner_board,
         numbers_not_drawn_per_board[winner_board_index][1:]))
) 
winning_number: int = numbers_not_drawn_per_board[winner_board_index][0]

print(sum_not_drawn_numbers * winning_number)