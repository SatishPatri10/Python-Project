import math
import random

lower_bound = int(input("Enter lower bound:-  "))
upper_bound = int(input("Enter upper bound:-  "))

random_number = random.randint(lower_bound, upper_bound)

min_guess = math.log(upper_bound - lower_bound+1, 2)

print("\n\tYou are having only ", round(min_guess), " chances.")

count = 0


while count < min_guess:
    count +=1

    guess = int(input("Guess a Number:- "))

    if random_number == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif random_number > guess:
        print("You guessed too small!")
    elif random_number < guess:
        print("You Guessed too high!")

if count >= min_guess:
    print("\nThe number is %d" % random_number)
    print("\tBetter Luck Next time!")