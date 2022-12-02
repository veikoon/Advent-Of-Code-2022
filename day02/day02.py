"""Second challenge of 2022 AOC"""

def read_input(filename:str):
    """Read file line by line"""
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.read().splitlines()
    lines = [l.split(' ') for l in lines]
    return lines


def chall_1(lines):
    """First challenge : 
        Calclulate the points following the strategy guide.
        While stipulate that X-Y-Z are Rock-Paper-Scissors.
    
    # A - X => Rock 
    # B - Y => Paper
    # C - Z => Scissors

    # Rock      > Scissors
    # Scissors  > Paper
    # Paper     > Rock

    # ord() allow us to grab the ASCII value of a Char.
    """

    points = 0
    for line in lines:
        points += ord(line[1]) - ord('X') + 1

        # If both chars minus their offset have the same value it's a draw.
        if ord(line[0]) - ord('A') == ord(line[1]) - ord('X'):
            points += 3

        # In Rock-Paper-Scissors (in this precise order)
        # if you play the element at the index (X+1)%3 you win. 
        elif (ord(line[0]) - ord('A') + 1) % 3 == ord(line[1]) - ord('X'):
            points += 6

    print("Day 02-1 : ", points)


def chall_2(lines):
    """Seconde challenge : 
        Calclulate the points following the strategy guide.
        While stipulate that X-Y-Z are Lose-Draw-win.
    
    # A => Rock 
    # B => Paper
    # C => Scissors

    # X => Lose
    # Y => Draw
    # Z => Win

    # Rock      > Scissors
    # Scissors  > Paper
    # Paper     > Rock

    # ord() allow us to grab the ASCII value of a Char.
    """
    points = 0
    for line in lines:

        # You need to play the element at the index (X-1)%3 to lose.
        if line[1] == 'X':
            points += (ord(line[0]) - ord('A') - 1) % 3  + 1

        # You need to play the element at the same index to draw.
        elif line[1] == 'Y':
            points += ord(line[0]) - ord('A') + 1
            points += 3

        # You need to play the element at the index (X+1)%3 to win.
        elif line[1] == 'Z':
            points += 6
            points += (ord(line[0]) - ord('A') + 1) % 3 + 1

    print("Day 02-2 : ", points)


if __name__ == "__main__":
    # Input file is read
    input_list = read_input("input.txt")
    chall_1(input_list)
    chall_2(input_list)
