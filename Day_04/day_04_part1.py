from Day_03.day_03_part1 import get_instructions as get_words


def main():

    words = get_words("wordsearch.txt").split("\n")
    grid = [list(row) for row in words]

    results = find_all_xmas(grid)
    print(len(results))


def find_all_xmas(grid, word="XMAS"):
    rows = len(grid)
    columns = len(grid[0])
    directions = [
        (0, 1),  # horizontal right
        (0, -1),  # horizontal left
        (1, 0),  # horizontal down
        (-1, 0),  # horizontal up
        (1, 1),  # diagonal down-right
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)  # diagonal up-right
    ]

    def search_from(hx, hy, dx, dy):
        for i, char in enumerate(word):
            nx, ny = hx + i * dx, hy + i * dy
            if not is_valid(nx, ny, rows, columns) or grid[nx][ny] != char:
                return False
        return True

    results = []
    for hx, row in enumerate(grid):
        for hy, cell in enumerate(row):
            if cell == word[0]:  # start search if X is first letter
                for dx, dy in directions:
                    if search_from(hx, hy, dx, dy):
                        results.append((hx, hy, dx, dy))

    return results


def is_valid(x, y, rows, columns):
    return 0 <= x < rows and 0 <= y < columns


if __name__ == "__main__":
    main()
