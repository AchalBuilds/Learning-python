
while True:
    number = int(input("Enter a number(999 to quit): "))

    if number == 999: 
        print("Program quitted successfully.")
        break

    if number == 0:
        print("The number is Zero!")
    elif number % 2 == 0:
        print(f"{number} is an even number!")
    else:
        print(f"{number} is an odd number!")