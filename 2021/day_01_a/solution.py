def count_increases() -> int:
    with open("input.txt", "r", encoding="UTF8") as inputfile:
        measurements = [int(line.strip()) for line in inputfile.readlines()]
    increases = []
    for i in range(1, len(measurements)):
        if measurements[i-1] < measurements[i]:
            increases.append(True)
        else:
            increases.append(False)
    return sum(increases)


print(count_increases())
