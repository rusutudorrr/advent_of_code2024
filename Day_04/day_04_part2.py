from Day_03.day_03_part1 import get_instructions as get_words
from day_04_part1 import is_valid


def main():

    words = get_words("wordsearch.txt").split("\n")
    grid = [list(row) for row in words]

    results = find_xmas_x(grid)
    print(len(results))


def find_xmas_x(grid):
    rows = len(grid)
    columns = len(grid[0])
    results = []

    # check for X-MAS at position (row, col)
    def check_x_mas(row, col):
        if (
            is_valid(row - 1, col - 1, rows, columns) and is_valid(row + 1, col + 1, rows, columns) and
            is_valid(row - 1, col + 1, rows, columns) and is_valid(row + 1, col - 1, rows, columns)
        ):
            top_left = grid[row - 1][col - 1]
            center = grid[row][col]
            bottom_right = grid[row + 1][col + 1]
            bottom_left = grid[row + 1][col - 1]
            top_right = grid[row - 1][col + 1]

            # Check both diagonals
            if ((top_left + center + bottom_right in ["MAS", "SAM"]) and (bottom_left + center + top_right in ["MAS", "SAM"])):
                return True
        return False

    # iterate through all cells in grid
    for row_idx, row in enumerate(grid[1:-1], start=1):  # avoid edges
        for col_idx, cell in enumerate(row[1:-1], start=1):
            if cell == 'A':  # center of X-MAS
                if check_x_mas(row_idx, col_idx):
                    results.append((row_idx, col_idx))

    return results

if __name__ == "__main__":
    main()
