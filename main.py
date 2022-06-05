from random import randint

#create a list of play options
choices = ["Rock", "Paper", "Scissors"]

#assign a random play to the cpu
cpu = choices[randint(0,2)]

#set opponent to False
opponent = False

while opponent == False:
#set opponent to True
    opponent = input("Rock, Paper, Scissors?")
    if opponent == cpu:
        print("Tie!")
    elif opponent == "Rock":
        if cpu == "Paper":
            print("You lose!", cpu, "covers", opponent)
        else:
            print("You win!", opponent, "smashes", cpu)
    elif opponent == "Paper":
        if cpu == "Scissors":
            print("You lose!", cpu, "cuts", opponent)
        else:
            print("You win!", opponent, "covers", cpu)
    elif opponent == "Scissors":
        if cpu == "Rock":
            print("You lose...", cpu, "smashes", opponent)
        else:
            print("You win!", opponent, "cuts", cpu)
    else:
        print("That's an invalid input. Ensure your input is initial capitalized!")
    #opponent was set to True, but we want it to be False so the loop continues
    opponent = False
    cpu = choices[randint(0,2)]