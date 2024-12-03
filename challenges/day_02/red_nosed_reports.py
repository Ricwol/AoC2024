import itertools as it


def main():
    reports = read_input('input.txt')

    safe_reports = sum(is_safe(report) for report in reports)
    print(f'{safe_reports} report(s) are safe.')

    safe_with_dampener = sum(with_tolerance(report) for report in reports)
    print(f'{safe_with_dampener} report(s) are safe with +1 tolerance.')


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


def with_tolerance(levels: list[int]) -> int:
    if is_safe(levels):
        return 1

    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i+1:]):
            return 1
    return 0


if __name__ == '__main__':
    main()
