import itertools as it


def main():
    reports = read_input('input.txt')

    safe_reports = sum(is_safe(report) for report in reports)
    print(f'{safe_reports} report(s) are safe.')


def read_input(filename: str) -> list[list[int]]:
    with open(filename) as file:
        return [[int(level) for level in line.split()] for line in file]


def is_safe(levels: list[int]) -> int:
    prior = 0
    for left, right in it.pairwise(levels):
        diff = left - right
        if not (1 <= abs(diff) <= 3) or (diff*prior < 0):
            return 0
        prior = diff
    return 1


if __name__ == '__main__':
    main()
