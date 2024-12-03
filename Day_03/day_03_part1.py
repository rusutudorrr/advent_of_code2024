import re


def main():
    instructions = get_instructions('instructions.txt')
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, instructions)

    total = sum(int(x) * int(y) for x, y in matches)
    print(total)


def get_instructions(file):
    with open(file, "r") as file:
        data = file.read()

    return data


if __name__ == "__main__":
    main()
