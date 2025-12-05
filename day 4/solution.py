def load_day_4_input():
    with open("puzzle_input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        line = line.strip("\n")
        if line:
            grid.append(line)

    return grid


def count_accessible_paper_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    neighbor_directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    total_accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbor_count = 0
            for dr, dc in neighbor_directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        neighbor_count += 1

            if neighbor_count < 4:
                total_accessible += 1

    return total_accessible


def count_total_removed_rolls(grid):
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    neighbor_directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue

                neighbor_count = 0
                for dr, dc in neighbor_directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            neighbor_count += 1

                if neighbor_count < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = "."

        total_removed += len(to_remove)

    return total_removed


def solve_part_1():
    grid = load_day_4_input()
    answer = count_accessible_paper_rolls(grid)
    print(f"Solution to part 1: {answer}")


def solve_part_2():
    grid = load_day_4_input()
    answer = count_total_removed_rolls(grid)
    print(f"Solution to part 1: {answer}")


def execute_day_4():
    solve_part_1()
    solve_part_2()


if __name__ == "__main__":
    execute_day_4()