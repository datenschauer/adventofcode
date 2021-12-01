def count_increases(inputfile: str) -> int:
    with open(inputfile, "r", encoding="UTF8") as inputfile:
        measurements = [int(line.strip()) for line in inputfile.readlines()]
    increases = []
    for i in range(3, len(measurements)):
        last_group = measurements[i - 3] + measurements[i - 2] + measurements[i - 1]
        actual_group = measurements[i - 2] + measurements[i - 1] + measurements[i]
        if last_group < actual_group:
            increases.append(True)
        else:
            increases.append(False)
    return sum(increases)


inputtxt = "input.txt"

print(count_increases(inputtxt))
