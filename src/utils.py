def compress(steps: str) -> str:
    """
    Compress all the moves

    Example:
        input = rrrddduuu
        return = r3d3u3

    :parm steps:  Characters
    :return A string that contains characters and single digit in betweeb the characters
    """
    index = 0
    compressed_steps = ""
    len_steps = len(steps)
    steps = steps.lower()
    for step in steps:
        if step not in ["r", "d", "u"]:
            raise Exception("Invalid direction")

    while index != len_steps:
        count = 1
        while (index < len_steps - 1) and (steps[index] == steps[index + 1]):
            count += 1
            index += 1
        if count == 1:
            compressed_steps += str(steps[index])
        else:
            compressed_steps += str(steps[index]) + str(count)
        index += 1
    return compressed_steps


def count_steps_for_next_move(steps: str) -> tuple:
    if len(steps) == 1:
        return steps[0], 1
    else:
        for index, step in enumerate(steps[:-1]):
            number_of_steps = 0
            if step == "r":
                if steps[index + 1].isdigit():
                    number_of_steps = int(steps[index + 1])
                else:
                    number_of_steps = 1
            if step == "u":
                if steps[index + 1].isdigit():
                    number_of_steps = int(steps[index + 1])
                else:
                    number_of_steps = 1
            if step == "d":
                if steps[index + 1].isdigit():
                    number_of_steps = int(steps[index + 1])
                else:
                    number_of_steps = 1
        return step, number_of_steps
