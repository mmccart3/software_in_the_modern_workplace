user_input = input("Please enter a number between 1 and 12 >")
for i in range(1, 13):
    try:
        x = i * int(user_input)
        print(x)
    except:
        print("Invalid input. Please enter a valid number.")