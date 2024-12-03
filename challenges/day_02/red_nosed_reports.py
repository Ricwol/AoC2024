def main():
    reports = read_input('input.txt')


def read_input(filename: str) -> list[list[int]]:
    with open(filename) as file:
        return [[int(level) for level in line.split()] for line in file]


if __name__ == '__main__':
    main()
