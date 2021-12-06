# https://adventofcode.com/2021/day/1
import itertools


#
# Puzzle #1
#


def count_single_measurement_increases(numbers):
    previous_number = None
    result = 0

    for number in numbers:
        if previous_number and number > previous_number:
            result += 1
        previous_number = number

    return result


def puzzle1():
    with open('day01.input.txt') as f:
        numbers = (int(line) for line in f.readlines())
        print(count_single_measurement_increases(numbers))


#
# Puzzle #2
#


def sliding_windows(iterable, window_size=3):
    iterables = itertools.tee(iterable, 3)

    for n in range(window_size):
        for _ in range(n):
            next(iterables[n])

    return zip(*iterables)


def count_windowed_measurement_increases(numbers):
    previous_window = None
    result = 0

    for window in sliding_windows(numbers, 3):
        if previous_window and sum(window) > sum(previous_window):
            result += 1
        previous_window = window

    return result


def puzzle2():
    with open('day01.input.txt') as f:
        numbers = (int(line) for line in f.readlines())
        print(count_windowed_measurement_increases(numbers))


#
# Entry Point
#


if __name__ == '__main__':
    print('#1:', puzzle1())
    print('#2:', puzzle2())
