boardtype = list[list]

boardlisttype = list[boardtype]


def read_randoms(inputfile) -> list[int]:
    with open(inputfile, "r", encoding="UTF8") as file:
        line: str = file.readline()
    return [int(element) for element in line.split(",")]


def read_boards(inputfile) -> boardlisttype:
    boards: boardlisttype = []

    with open(inputfile, "r", encoding="UTF8") as file:
        stringlist: list[str] = file.readlines()

    for i in range(1, len(stringlist), 6):
        board: boardtype = []
        for j in range(1, 6):
            board.append(
                # a string line like "40  0 30 48 76\n" (beware of double space before 0!!)
                # is cast to a list of integers: [40, 0, 30, 48, 76]
                [int(char) for char in stringlist[i + j].strip().replace("  ", " ").split(" ")]
            )
        boards.append(board)

    return boards


def mark_boards(boards: boardlisttype, random: int) -> None:
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == random:
                    row[i] = "x"


def check_boards(boards: boardlisttype) -> (bool, boardtype):
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

    return_board = None
    won = False

    for board in boards:
        won = check_rows(board)
        if won:
            return_board = board
            break
        won = check_cols(board)
        if won:
            return_board = board
            break

    return won, return_board


def calc_winning_board(board: boardtype) -> int:
    return sum([sum([i for i in row if i != "x"]) for row in board])


# execute Program
randoms = read_randoms("input.txt")

boardlist = read_boards("input.txt")

for integer in randoms:
    mark_boards(boardlist, integer)
    won, winning_board = check_boards(boardlist)
    if won:
        # print(calc_winning_board(winning_board) * integer)
        print("Winner!", integer, winning_board)
        print("Solution: ", calc_winning_board(winning_board) * integer)
        break
