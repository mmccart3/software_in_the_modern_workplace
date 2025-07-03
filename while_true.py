user_input = input("please enter 1, 2 or 3 >").strip()

while True:
    if user_input == '1' or user_input == '2' or user_input == '3':
        break
    else:
        print("Invalid input")
        user_input = input("please enter 1, 2 or 3 >").strip()

print(f"You chose {user_input}")
