import random 

print("Let's Play Rock Paper Scissors!")
​
# Specify the three options
options = ["r", "p", "s"]
​
# Computer Selection
computer_choice = random.choice(options)
​
# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

if user_choice = computer_choice:
    print("Tie!")
elif user_choice == "r" and computer_choice == "s":
    print("User wins!")
elif user_choice == "r" and computer_choice == "p":
    print("Computer winS!")
elif user_choice == "p" and computer_choice == "r":
    print("")

