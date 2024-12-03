from day_01_part1 import generate_data


def main():

    locations_left, locations_right = generate_data()
    calculate_similarity(locations_left, locations_right)


def calculate_similarity(locations_left, locations_right):

    distances = []

    for loc in locations_left:
        count = 0
        for joc in locations_right:
            if loc == joc:
                count += 1
        distances.append(int(loc) * count)

    print(sum(distances))
    return sum(distances)


if __name__ == "__main__":
    main()
