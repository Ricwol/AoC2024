def main():
    left: list[int] 
    right: list[int]

    left, right = read_input(filename='./input.txt')
    total_distance = get_total_distance(left, right)
    similarity_score = get_similarity_score(left, right)

    print(f'Total distance: {total_distance}')
    print(f'Similarity score: {similarity_score}')


def read_input(filename: str) -> tuple[list, list]:
    left: list[int] = []
    right: list[int] = []

    with open(filename) as file:
        for line in file:
            l, r = [int(val) for val in line.strip().split()]
            left.insert(at(left, l), l)
            right.insert(at(right, r), r)
    return left, right


def at(locations: list[int], number):
    for pos, location_id in enumerate(locations):
        if number <= location_id:
            return pos
    return len(locations)


def get_total_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(l-r) for l, r in zip(left, right))


def get_similarity_score(left: list[int], right: list[int]) -> int:
    return sum(right.count(l)*l for l in left)    


if __name__ == '__main__':
    main()

