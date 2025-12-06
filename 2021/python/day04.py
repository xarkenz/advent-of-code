from utils import *

start_time: float = get_start_time()

first_line, _, *lines = get_input_lines("day04.txt")
call_order: list[int] = [int(number) for number in first_line.split(",")]
bingo_boards: list[list[list[int]]] = []

current_board: list[list[int]] = []
for line in lines:
    if line:
        current_board.append([int(number) for number in line.split()])
    else:
        bingo_boards.append(current_board)
        current_board = []

def has_bingo(board: list[list[int]], called: list[bool]) -> bool:
    return (
        # Check rows
        any(all(called[number] for number in row) for row in board) or
        # Check columns
        any(all(called[number] for number in column) for column in zip(*board)) or
        # Check one diagonal
        all(called[board[i][i]] for i in range(len(board))) or
        # Check the other diagonal
        all(called[board[i][-(i + 1)]] for i in range(len(board)))
    )

def sum_unmarked(board: list[list[int]], called: list[bool]) -> int:
    return sum(number for row in board for number in row if not called[number])

called: list[bool] = [False] * (max(call_order) + 1)
first_final_score: Optional[int] = None
last_final_score: Optional[int] = None

for call_number in call_order:
    called[call_number] = True
    next_bingo_boards: list[list[list[int]]] = []
    for board in bingo_boards:
        if has_bingo(board, called):
            if first_final_score is None:
                first_final_score = sum_unmarked(board, called) * call_number
        else:
            next_bingo_boards.append(board)
    if not next_bingo_boards:
        last_final_score = sum_unmarked(bingo_boards[0], called) * call_number
        break
    bingo_boards = next_bingo_boards

print("[04p1] First winning final score:", first_final_score)
print("[04p2] Last winning final score:", last_final_score)

print_time_elapsed(start_time)
