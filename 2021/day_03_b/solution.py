import pandas as pd


def convert_input_to_matrix(inputfile):
    """
    convert input strings to a matrix of ones and zeros like:
    [[1, 0, 1]
     [0, 0, 1]
     [1, 0, 0]]
    """
    with open(inputfile, "r", encoding="UTF8") as file:
        string_list = [line.strip() for line in file.readlines()]

    return [[int(char) for char in string_list[i]] for i in range(len(string_list))]


def calc_rate(list_of_bits, most_common=True):
    """
    get a list of lists of zeros and ones
    convert them to a dataframe
    reduce dataframe until only one row left
    return the integer value of remaining row of bits
    """
    if most_common:
        bigger = 1
        fewer = 0
    else:
        bigger = 0
        fewer = 1

    df = pd.DataFrame(list_of_bits)

    remaining_rows = df[0].count()
    i = 0

    while remaining_rows > 1:
        if df[i].sum() > df[i].count() / 2:
            df = df[df[i] == bigger]
        elif df[i].sum() < df[i].count() / 2:
            df = df[df[i] == fewer]
        else:
            df = df[df[i] == bigger]

        remaining_rows = df[0].count()
        i += 1

    bitstring = "".join([str(integer) for integer in df.values[0].tolist()])

    return int(bitstring, 2)


input_list = convert_input_to_matrix("input.txt")


oxygen = calc_rate(input_list, most_common=True)

co2 = calc_rate(input_list, most_common=False)

print(oxygen * co2)
