def best_k_digits(joltage, k):
    digits = [int(ch) for ch in joltage]
    n = len(digits)
    if k >= n:
        return digits[:]

    remove = n - k
    stack: list[int] = []

    for d in digits:
        while remove and stack and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    while remove:
        stack.pop()
        remove -= 1

    return stack[:k]


def fetch_k_largest_ints(k):
    with open("puzzle_input.txt", "r") as file:
        joltages = file.readlines()

    results = {}
    for line in joltages:
        joltage = line.rstrip("\n")
        best_digits = best_k_digits(joltage, k)
        results[joltage] = best_digits

    return results


def calculate_total_output_joltage(results):
    total_output = 0
    for joltage, digits in results.items():
        joltage_str = "".join(str(d) for d in digits)
        total_output += int(joltage_str)
    return total_output


def solve_part_1():
    results_dict = fetch_k_largest_ints(2)
    total_output = calculate_total_output_joltage(results_dict)
    print(f"Total output joltage for challenge 1: {total_output}")


def solve_part_2():
    results_dict = fetch_k_largest_ints(12)
    total_output = calculate_total_output_joltage(results_dict)
    print(f"Total output joltage for challenge 2: {total_output}")


def execute_day_3():
    solve_part_1()
    solve_part_2()


if __name__ == "__main__":
    execute_day_3()
