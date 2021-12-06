# https://adventofcode.com/2021/day/2


#
# Puzzle #1
#


def move(lines):
    horizontal_pos = 0
    depth = 0

    for line in lines:
        command, argument = line.split(maxsplit=1)
        if command == 'forward':
            horizontal_pos += int(argument)
        elif command == 'down':
            depth += int(argument)
        elif command == 'up':
            depth -= int(argument)

    return (horizontal_pos, depth)


def puzzle1():
    with open('day02.input.txt') as f:
        horizontal_pos, depth = move(f.readlines())
        print(horizontal_pos * depth)


#
# Puzzle #2
#


def move2(lines):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for line in lines:
        command, argument = line.split(maxsplit=1)
        if command == 'forward':
            horizontal_pos += int(argument)
            depth += int(argument) * aim
        elif command == 'down':
            aim += int(argument)
        elif command == 'up':
            aim -= int(argument)

    return (horizontal_pos, depth)


def puzzle2():
    with open('day02.input.txt') as f:
        horizontal_pos, depth = move2(f.readlines())
        print(horizontal_pos * depth)


#
# Entry Point
#


if __name__ == '__main__':
    print('#1:', puzzle1())
    print('#2:', puzzle2())
