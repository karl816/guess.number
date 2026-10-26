import random

lowest_number = 0
highest_number = 10
number = random.randint(lowest_number, highest_number)

print("GUESSING NUMBER GAME")
print(f"CHOOSE A NUMBER BETWEEN {lowest_number} and {highest_number}")

while True:
    num = input("Select a number between 0-10: ")
    if num.isdigit():
        num = int(num)
        if num > highest_number or num < lowest_number:
            print("You have to choose a number in the range")
        elif num > number:
            print("Too high!")
        elif num < number:
            print("Too low!")
        else:
            print("Correct!")
            break







