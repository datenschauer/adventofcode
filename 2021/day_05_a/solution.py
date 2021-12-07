import numpy as np


def read_coords(inputfile):
    with open(inputfile, "r", encoding="UTF8") as file:
        stringlist = file.readlines()

    list_of_coords = []

    for line in stringlist:
        coords = [[int(char) for char in part.split(",")] for part in line.split(" -> ")]
        if (coords[0][0] == coords[1][0]) | (coords[0][1] == coords[1][1]):
            list_of_coords.append(coords)

    return list_of_coords


def mark_points(matrix, list_of_coords):
    for coords in list_of_coords:
        start = coords[0]
        end = coords[1]
        # Case 1: horizontal line (x1 == x2)
        if (start[0] == end[0]) & (start[1] < end[1]):
            for i in range(- (start[1] - end[1]) + 1):
                matrix[start[0], start[1] + i] += 1

        elif (start[0] == end[0]) & (start[1] > end[1]):
            for i in range((start[1] - end[1]) + 1):
                matrix[start[0], start[1] - i] += 1

        # Case 2: vertical line (y1 == y2)
        elif (start[1] == end[1]) & (start[0] < end[0]):
            for i in range(- (start[0] - end[0]) + 1):
                matrix[start[0] + i, end[1]] += 1

        elif (start[1] == end[1]) & (start[0] > end[0]):
            for i in range((start[0] - end[0]) + 1):
                matrix[start[0] - i, start[1]] += 1

    return matrix


def calc_solution(matrix) -> int:
    return np.count_nonzero(matrix > 1)


coords = read_coords("input.txt")

matrix = np.zeros((1000, 1000))

new_matrix = mark_points(matrix, coords)

print(calc_solution(matrix))
