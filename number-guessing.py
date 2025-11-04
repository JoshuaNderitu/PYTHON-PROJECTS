import random


print(" Welcome to the number guessing game.")

#let the user choose the range 
low = int(input("Enter the low number in range: "))
high = int(input("Enter the high number in range: "))

print("You have 7 attempts to guess the number. Good luck")

num = random.randint(low, high) # generate a random number
g_counter = 0
chance = 7

while g_counter < chance:  #the loop will always run aslong as g_counter is less than chance
    g_counter += 1
    guess = int(input("What do you think is the number? "))

    if guess == num:
        print(f"Congratulations. You got the number right in {g_counter} chances")
        break

    elif g_counter >= chance and guess != num: #loop breaks if the chances are up
        print(f"You Lost. The number was {num}. Try again next time.")
        
    elif guess < num:
        print("Sorry the number is too low. Try again...")
        
    
    elif guess > num:
        print("Sorry the number is too high. Try again...")
        
    
    


