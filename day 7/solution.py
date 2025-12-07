

def fetch_input():
    with open("puzzle_input.txt", "r") as f:
        raw_data = f.readlines()
    
    parsed_data = []
    for i in range(len(raw_data)):
        parsed_data.append(raw_data[i].strip())
    
    return parsed_data


def calculate_start_and_splitters(data):
    start_index = 0
    for i in range(len(data[0])):
        if data[0][i] == "S":
            start_index = i

    splitters_index = []
    for i in range(len(data)):
        splitters_index.append([])
        for k in range(len(data[i])):
            if data[i][k] == "^":
                splitters_index[i].append(k)
    
    return start_index, splitters_index


def calculate_amount_of_beam_splits(start_index, splitters_index):
    beam_splits = 0
    beam_indexes = set([start_index])

    for i in range(len(splitters_index)):
        row_splitters = splitters_index[i]
        new_beam_indexes = set()

        for j in range(len(row_splitters)):
            splitter_index = row_splitters[j]
            if splitter_index in beam_indexes:
                beam_splits += 1
                new_beam_indexes.add(splitter_index - 1)
                new_beam_indexes.add(splitter_index + 1)

        for beam_index in beam_indexes:
            if beam_index not in row_splitters:
                new_beam_indexes.add(beam_index)

        beam_indexes = new_beam_indexes

    return beam_splits


def calculate_amount_of_timelines(start_index, splitters_index, width):
    timeline_indexes = [0] * width
    timeline_indexes[start_index] = 1

    timelines_exited = 0
    last_row_index = len(splitters_index) - 1

    for i in range(len(splitters_index)):
        row_splitters = splitters_index[i]
        new_timeline_indexes = [0] * width

        for col in range(width):
            timeline_count = timeline_indexes[col]
            if timeline_count == 0:
                continue

            is_splitter = False
            for s in row_splitters:
                if s == col:
                    is_splitter = True
                    break

            if is_splitter:
                if col - 1 >= 0:
                    new_timeline_indexes[col - 1] += timeline_count
                else:
                    timelines_exited += timeline_count

                if col + 1 < width:
                    new_timeline_indexes[col + 1] += timeline_count
                else:
                    timelines_exited += timeline_count
            else:
                if i == last_row_index:
                    timelines_exited += timeline_count
                else:
                    new_timeline_indexes[col] += timeline_count

        timeline_indexes = new_timeline_indexes

    return timelines_exited
    




def solve_part_1():
    data = fetch_input()
    start, splitters = calculate_start_and_splitters(data)
    amount_of_beams_splits = calculate_amount_of_beam_splits(start, splitters)
    print(f"Solution to challenge 1: {amount_of_beams_splits}")


def solve_part_2():
    data = fetch_input()
    start, splitters = calculate_start_and_splitters(data)
    width = len(data[0])
    amount_of_timelines = calculate_amount_of_timelines(start, splitters, width)
    print(f"Solution to challenge 2: {amount_of_timelines}")


def execute_day_7():
    solve_part_1()
    solve_part_2()


if __name__ == "__main__":
    execute_day_7()