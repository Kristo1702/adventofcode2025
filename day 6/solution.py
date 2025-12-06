def fetch_and_parse_input():
    columns = []

    with open("puzzle_input.txt", "r") as f:
        for line in f:
            values = line.strip().split()

            if not columns:
                columns = [[] for _ in range(len(values))]

            for i, v in enumerate(values):
                columns[i].append(v)

    return columns

def calculate_columns_part_1(columns):
    total_results = []
    for column in columns:

        result_column_addition = 0
        result_column_multiplikation = 1
        operator = ""
        numbers = []

        for element in column:
            if element in ["+", "*"]:
                operator = element
            else:
                numbers.append(int(element))
        
        for number in numbers:
            if operator == "+":
                result_column_addition += number
            elif operator == "*":
                result_column_multiplikation *= number

        if operator == "+":
            total_results.append(result_column_addition)
        elif operator == "*":
            total_results.append(result_column_multiplikation)

    
    return sum(total_results)

def calculate_columns_part_2(columns):
    with open("puzzle_input.txt", "r") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    if not raw_lines:
        return 0

    height = len(raw_lines)
    width = max(len(line) for line in raw_lines)

    lines = [line.ljust(width) for line in raw_lines]

    problems = []
    current_problem = []

    for x in range(width):
        column_chars = [lines[y][x] for y in range(height)]
        if all(ch == " " for ch in column_chars):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(column_chars)

    if current_problem:
        problems.append(current_problem)

    grand_total = 0

    for problem in problems:
        operator = None
        for col in problem:
            ch = col[-1]
            if ch in ["+", "*"]:
                operator = ch
                break

        if operator is None:
            continue

        numbers = []
        for col in problem:
            digits = "".join(ch for ch in col[:-1] if ch != " ")
            if digits:
                numbers.append(int(digits))

        numbers = list(reversed(numbers))

        if operator == "+":
            result = sum(numbers)
        elif operator == "*":
            result = 1
            for n in numbers:
                result *= n
        else:
            continue

        grand_total += result

    return grand_total



def solve_part_1():
    columns = fetch_and_parse_input()
    part_1_solution = calculate_columns_part_1(columns)
    print(f"Solution to challenge 1: {part_1_solution}")


def solve_part_2():
    columns = fetch_and_parse_input()
    part_2_solution = calculate_columns_part_2(columns)
    print(f"Solution to challenge 2: {part_2_solution}")


def execute_day_6():
    solve_part_1()
    solve_part_2()


if __name__ == "__main__":
    execute_day_6()