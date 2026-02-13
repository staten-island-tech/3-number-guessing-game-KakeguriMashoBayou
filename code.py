import random 
nums = ["1","2","3","4","5","6","7","8","9","10"]
guess = random.choice(nums)
user = input("Guess the Number")

while user != "guess":
    guess = input("guess a number from 1 to 10")
    if guess == "5":
        print(guess, "correct")
    elif guess < "5" :
        print(guess, "incorrect go higher")




