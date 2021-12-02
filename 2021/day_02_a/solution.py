def get_position(inputfile):
    """
    Output the horizontal and vertical position of the submarine.
    """
    with open(inputfile, "r", encoding="UTF8") as inputfile:

        movements = [line.strip() for line in inputfile.readlines()]

    hpos = 0
    vpos = 0

    for movement in movements:
        if movement[0] == "f":
            hpos += int(movement[-1])
        elif movement[0] == "d":
            vpos += int(movement[-1])
        else:
            vpos -= int(movement[-1])

    return hpos, vpos


horizontal, depth = get_position("input.txt")

print(horizontal * depth)
