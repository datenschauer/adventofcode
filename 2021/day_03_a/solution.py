import pandas as pd


def invert_bit_string(string):
    """
    return the invert of a string of bits
    '1001' -> '0110' | '1010' -> '0101'
    """
    bools = [bool(int(char)) for char in string]
    return "".join([str(int(not boolean)) for boolean in bools])


def convert_input_to_matrix(inputfile):
    """
    convert input strings to a matrix of charcters of ones and zeros like:
    [[1, 0, 1]
     [0, 0, 1]
     [1, 0, 0]]
    """
    with open(inputfile, "r", encoding="UTF8") as file:
        string_list = [line.strip() for line in file.readlines()]

    return [[int(char) for char in string_list[i]] for i in range(len(string_list))]


def calc_gamma_and_epsilon_rates(list_of_bits):
    """
    get a list of lists of zeros and ones
    convert them to a dataframe
    count 0s and 1s of every column and generate gamma and epsilon rates
    """
    df = pd.DataFrame(list_of_bits)

    gamma_rate = ""

    for i in range(len(df.columns)):
        if df[i].sum() > df[i].count() / 2:
            gamma_rate += "1"
        else:
            gamma_rate += "0"

    epsilon_rate = invert_bit_string(gamma_rate)

    return gamma_rate, epsilon_rate


# testinput = [[1, 1, 1],
#             [0, 0, 0],
#             [1, 0, 1]]
# testoutput = calc_gamma_and_epsilon_rates(testinput)
# tesoutput should be ('1, 0, 1', '0, 1, 0')

bits_list = convert_input_to_matrix("input.txt")

gamma, epsilon = calc_gamma_and_epsilon_rates(bits_list)

# in python strings of bits can be converted with the builtin int function given a number for the base argument
# see: https://docs.python.org/3/library/functions.html#int
print(int(gamma, 2) * int(epsilon, 2))
