from collections import defaultdict


def read_randoms(inputfile) -> list[int]:
    with open(inputfile, "r", encoding="UTF8") as file:
        line: str = file.readline()
    return [int(element) for element in line.split(",")]


def read_boards(inputfile):
    boards = defaultdict(int)

    with open(inputfile, "r", encoding="UTF8") as file:
        stringlist: list[str] = file.readlines()
    key = 0
    for i in range(1, len(stringlist), 6):
        board = []
        for j in range(1, 6):
            board.append(
                # a string line like "40  0 30 48 76\n" (beware of double space before 0!!)
                # is cast to a list of integers: [40, 0, 30, 48, 76]
                [int(char) for char in stringlist[i + j].strip().replace("  ", " ").split(" ")]
            )

        boards[key] = {"winner": False, "board": board}
        key += 1

    return boards


def mark_boards(boards, random: int) -> None:
    for item in boards.items():
        for row in item[1]["board"]:
            for j in range(len(row)):
                if row[j] == random:
                    row[j] = "x"


def check_boards(boards):
    # winning condition 1: a whole row is marked with "x"
    def check_rows(board) -> bool:
        won = False
        for row in board:
            if len([i for i in filter(lambda x: x == "x", row)]) == 5:
                won = True
                break
        return won

    # winning condition 2: a whole column is marked with "x"
    def check_cols(board) -> bool:
        won = False
        for i in range(len(board[0])):
            col_to_check = []
            for row in board:
                col_to_check.append(row[i])
            if len([i for i in filter(lambda x: x == "x", col_to_check)]) == 5:
                won = True
                break
        return won

    last_board = None

    for item in boards.items():
        actual_board = item[1]["board"]
        won = check_rows(actual_board)
        if won:
            last_board = actual_board
            item[1]["winner"] = True
        else:
            won = check_cols(actual_board)
            if won:
                last_board = actual_board
                item[1]["winner"] = True

    return last_board


def filter_boards(boards):
    return {k: v for k, v in boards.items() if v["winner"] is False}


def calc_winning_board(board) -> int:
    return sum([sum([i for i in row if i != "x"]) for row in board])


# execute Program
randoms = read_randoms("input.txt")

boardlist = read_boards("input.txt")

last_board = None
last_integer = 0

for integer in randoms:
    mark_boards(boardlist, integer)
    check = check_boards(boardlist)
    if check is not None:
        last_board = check
        last_integer = integer
    boardlist = filter_boards(boardlist)

print("Last Winner: ", last_board)
print("Last Integer: ", last_integer)
print("Solution: ", calc_winning_board(last_board) * last_integer)
