def is_invalid_id(n: int) -> bool:
    s = str(n)

    if s[0] == "0":
        return False

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


def is_invalid_id_part_2(n: int) -> bool:
    s = str(n)

    if s[0] == "0":
        return False

    length = len(s)

    for block_len in range(1, length // 2 + 1):
        if length % block_len != 0:
            continue

        repeats = length // block_len
        if repeats < 2:
            continue

        block = s[:block_len]
        if block * repeats == s:
            return True

    return False


def parse_ranges(line):
    ranges = []
    line = line.strip()
    parts = line.split(",")
    for part in parts:
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


def sum_invalid_ids(line):
    ranges = parse_ranges(line)
    total = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    return total


def sum_invalid_ids_part_2(line):
    ranges = parse_ranges(line)
    total = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id_part_2(n):
                total += n

    return total


def solve_part_1(line):
    answer = sum_invalid_ids(line)
    print("Solution part 1:", answer)


def solve_part_2(line):
    answer = sum_invalid_ids_part_2(line)
    print("Solution part 2:", answer)


def execute_day_2():
    with open("puzzle_input.txt", "r") as f:
        line = f.read().strip()

    solve_part_1(line)
    solve_part_2(line)


if __name__ == "__main__":
    execute_day_2()