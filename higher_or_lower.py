import random
random_num = random.randint(1, 100)

print(f"The random number is between 1 and 100.")

while True:
    try:
        chance = int(input("Enter your guess: "))
        break
    except ValueError:
        print("Error. You must type a number.")

attempt = 1

while chance != random_num and attempt < 5:
    if chance < random_num:
        print("The random number is higher.")
    elif chance > random_num:
        print("The random number is lower.")
    try:
        chance = int(input("Enter your guess: "))
        attempt += 1
    except ValueError:
        print("Error. You must type a number.")

if chance == random_num:
    print(f"You won! The random number was {random_num}.")
    exit()

if chance != random_num:
    print(f"You ran out of attempts. The random number was {random_num}.")
    exit()