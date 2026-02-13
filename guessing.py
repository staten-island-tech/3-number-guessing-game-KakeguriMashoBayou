import random 
nums = ["1","2","3","4","5","6","7","8","9","10"]
guess = random.choice(nums)
user = input("Guess the Number")



your_guesses=[]

user1= ""
while user1 != int(guess):
    user1=int(input("Guess the Number:"))
    incorrect.append (user1)
    if user1 == int(guess):
        print("The Number is", guess) 
        print("Your guesses are", incorrect)
    else:
        print ("incorrect")
        if int(guess) > int(5):
            print("go higher")
        else: print("lower")
