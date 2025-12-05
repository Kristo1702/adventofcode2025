



def fetch_and_split_input():
    with open("puzzle_input.txt", "r") as f:
        raw_input = f.readlines()

    break_index = 0
    ranges = []
    for i in range(len(raw_input)):
        if raw_input[i] == "\n":
            break_index = i
            break
        ranges.append(raw_input[i].strip())
    
    ingredients = []
    for i in range(len(raw_input) - (break_index + 1)):
        ingredients.append(raw_input[break_index + i + 1].strip())
    
    return ranges, ingredients

def check_ingredients(ranges, ingredients):
    fresh_ingredients = 0
    for i in range(len(ingredients)):
        current_ingredient = ingredients[i]
        for i in range(len(ranges)):
            range_start, range_end = ranges[i].split("-")
            if int(current_ingredient) >= int(range_start) and int(current_ingredient) <= int(range_end):
                fresh_ingredients += 1
                break
    
    return fresh_ingredients

def get_unified_range_amount(ranges):
    intervals = []
    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        intervals.append((start, end))

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end + 1:
            if end > current_end:
                current_end = end
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    total = 0
    for start, end in merged:
        total += end - start + 1

    return total







def solve_part_1():
    ranges, ingredients = fetch_and_split_input()
    solution = check_ingredients(ranges, ingredients)
    print(f"Solution to part 1: {solution}")

def solve_part_2():
    ranges, ingredients = fetch_and_split_input()
    solution = get_unified_range_amount(ranges)
    print(f"Solution to part 2: {solution}")

def execute_day_5():
    solve_part_1()
    solve_part_2()

if __name__ == "__main__":
    execute_day_5()