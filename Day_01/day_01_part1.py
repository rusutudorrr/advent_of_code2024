def main():

    locations_left, locations_right = generate_data()
    calculate_distance(locations_left, locations_right)


def get_data(file):
    with open(file, 'r') as file:
        data = file.read().split()

    return data


def generate_data():

    locations_left = []
    locations_right = []

    for idx, item in enumerate(get_data('locations.txt'), start=1):
        if idx % 2 == 0:
            locations_right.append(item)
        else:
            locations_left.append(item)

    return locations_left, locations_right


def calculate_distance(locations_left, locations_right):

    distances = []

    while len(locations_left) and len(locations_right):
        current_min_left = min(locations_left)
        current_min_right = min(locations_right)

        distance = int(current_min_right) - int(current_min_left)
        distances.append(abs(distance))

        locations_right.remove(current_min_right)
        locations_left.remove(current_min_left)

    print(sum(distances))
    return sum(distances)


if __name__ == "__main__":
    main()
