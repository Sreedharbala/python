import random

top_of_range=input("enter a number! ")

if top_of_range.isdigit():
    top_of_range= int(top_of_range)

    if top_of_range <= 0:
        print("enter a value greater than zero")
        quit()
else:
    print("enter the digit number")

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time")
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess < random_number:
        print("the value is below the random number")
    else:
        print("you are above the number")

print("you got after", guesses, "guesses")

