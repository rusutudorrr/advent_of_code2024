def main():
    sequences = get_sequences('sequences.txt')
    safe_reports = run_rules(sequences)
    print(len(safe_reports))


def get_sequences(file):
    with open(file, "r") as file:
        return [[int(num) for num in line.strip().split()] for line in file if line.strip()]


def run_rules(data):
    return [is_safe(sequence) for sequence in data if is_safe(sequence)]


def is_safe(sequence):

    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    if all(1 <= diff <= 3 for diff in differences):  # increasing sequence
        return True
    elif all(-3 <= diff <= -1 for diff in differences):  # decreasing sequence
        return True
    return False


if __name__ == "__main__":
    main()
