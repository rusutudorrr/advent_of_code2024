from day_02_part1 import get_sequences, is_safe


def main():
    sequences = get_sequences()
    safe_reports = run_rules(sequences)
    print(len(safe_reports))


def run_rules(data):
    safe_reports = []
    for sequence in data:
        if is_safe(sequence):  # check if seq is safe as is
            safe_reports.append(sequence)
        else:
            # Check if removing one level makes it safe
            for i in range(len(sequence)):
                temp_sequence = sequence[:i] + sequence[i + 1:]  # start removing levels
                if is_safe(temp_sequence):
                    safe_reports.append(sequence)
                    break  # stop checking once it's safe

    return safe_reports


if __name__ == "__main__":
    main()
