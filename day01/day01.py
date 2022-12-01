"""First challenge of 2022 AOC"""

def read_input(filename:str):
    """Read file line by line"""
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.read().splitlines()
    return lines


def chall_01(lines:list):
    """First challenge : Find the maximum total of calories owned by an elf"""

    total_cal = 0
    total_list = []
    for line in lines:

        # If the line is empty, the total is added to a list and reset
        if not line:
            total_list.append(total_cal)
            total_cal = 0
            continue

        # Else we add the amount of this line to the total
        total_cal += int(line)

    print("Day 01-1 : ", max(total_list))

    return total_list


def chall_02(total_list:list):
    """Second challenge of the day : Find the 3 maximum"""
    total_list_sorted = sorted(total_list, reverse=True)
    max_3_total = total_list_sorted[:3]
    print("Day 01-2 : ", sum(max_3_total))


if __name__ == "__main__":

    # Input file is read
    input_list = read_input("input.txt")
    liste_max_cal = chall_01(input_list)
    chall_02(liste_max_cal)
