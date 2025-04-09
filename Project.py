import random

'''
1 for Rock
-1 for Paper
0 for Scissors
'''


computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (r for Rock , p for Paper , s for Scissors): ").lower()


youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}


if youstr not in youDict:
    print("Invalid choice! Please choose 'r', 'p', or 's'.")
else:
    
    you = youDict[youstr]

    
    print(f"Your choice: {reverseDict[you]}\nComputer's choice: {reverseDict[computer]}")

    
    if computer == you:
        print("It's a draw!")
    else:
        if (computer == 1 and you == -1) or (computer == 0 and you == 1) or (computer == -1 and you == 0):
            print("You win!!")
        else:
            print("You lose!!")
