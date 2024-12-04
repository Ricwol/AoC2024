import operator as op
import re

from collections.abc import Generator
from functools import reduce

REGEX_MUL = r'mul\(\d{1,3},\d{1,3}\)'
REGEX_ENABLE = '|'.join((REGEX_MUL, r'don\'t\(\)', r'do\(\)'))


def main() -> None:
    corrupted_memory = read_input('input.txt')
    result = scan(corrupted_memory, REGEX_MUL)
    print(f'The result of the multiplication: {result:_}')

    enabled_results = scan(corrupted_memory, REGEX_ENABLE)
    print(
        f'The result of only the enabled multiplication: {enabled_results:_}'
    )


def read_input(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def scan(memory: str, regex: str) -> int:
    return sum(map(mul, filter_instructions(memory, regex)))


def mul(instruction: str) -> int:
    return reduce(op.mul, map(int, re.findall(r'\d+', instruction)))


def filter_instructions(memory: str, regex: str) -> Generator[str, None, None]:
    enabled = True
    for instruction in re.findall(regex, memory):
        if instruction == 'don\'t()':
            enabled = False
        elif instruction == 'do()':
            enabled = True
        
        if enabled and instruction.startswith('m'):
            yield instruction


if __name__ == '__main__':
    main()
