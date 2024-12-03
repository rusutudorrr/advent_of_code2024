import re


def main():
    instructions = get_instructions('instructions.txt')
    pattern = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"

    enabled = True
    total = 0

    multiplications = re.finditer(pattern, instructions)

    for mul in multiplications:
        match = mul.group()
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled and match.startswith("mul"):
            x, y = map(int, mul.groups()[1:])
            total += x * y

    print(total)


def get_instructions(file):
    with open(file, "r") as file:
        data = file.read()

    return data


if __name__ == "__main__":
    main()
