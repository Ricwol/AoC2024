import operator as op
import re

from functools import reduce

REGEX = r'mul\(\d{1,3},\d{1,3}\)'


def main() -> None:
    corrupted_memory = read_input('input.txt')
    result = scan(corrupted_memory, REGEX)
    print(f'The result of the multiplication: {result:_}')


def read_input(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def scan(memory: str, regex: str) -> int:
    return sum(mul(instruction) for instruction in re.findall(regex, memory))


def mul(instruction: str) -> int:
    return reduce(op.mul, map(int, re.findall(r'\d+', instruction)))


if __name__ == '__main__':
    main()
