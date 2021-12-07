from collections import Counter


def read_list(inputfile):
    with open(inputfile, "r", encoding="UTF8") as file:
        return [int(char) for char in file.readline().split(",")]


def gen_fish(inputlist, integer):
    for day in range(integer):
        c = Counter(inputlist)
        inputlist = [i - 1 if i > 0 else i + 6 for i in inputlist]
        for i in range(c[0]):
            inputlist.append(8)
    return inputlist


inputlist = read_list("input.txt")

generated = gen_fish(inputlist, 80)

print(len(generated))
