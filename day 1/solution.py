# CHALLENGE 1
def decrypt_1():
    with open("file_with_password.txt", "r") as file:
        password_connections = file.readlines()

    final_password = 0
    dial_position = 50  # starter på 50

    for connection in password_connections:
        direction = connection[0]
        amount = int(connection[1:])

        if direction == "L":
            dial_position = (dial_position - amount) % 100
        elif direction == "R":
            dial_position = (dial_position + amount) % 100

        if dial_position == 0:
            final_password += 1

    return final_password



# CHALLENGE 2
def decrypt_2():
    with open("file_with_password.txt", "r") as file:
        password_connections = file.readlines()

    final_password = 0
    dial_position = 50

    for connection in password_connections:
        direction = connection[0]
        amount = int(connection[1:])

        while amount > 0:
            if direction == "R":
                dial_position += 1
            elif direction == "L":
                dial_position -= 1

            dial_position %= 100

            if dial_position == 0:
                final_password += 1

            amount -= 1

    return final_password





def execute_day_1():
    print(f"\n\nPassword for challenge 1: {decrypt_1()}") # CHALLENGE 1
    print(f"Password for challenge 2: {decrypt_2()}\n\n") # CHALLENGE 2


if __name__ == "__main__":
    execute_day_1()