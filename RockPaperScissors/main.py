import sys
import random
import os
os.system("")
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)




while True:
    print(Fore.BLUE + "==============\nRock Paper Scissors\n==============")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("==============")


    prompt = Fore.BLUE + "Please choose a number between 1-3:\n (   )\033[3D"
    player = int(input(prompt))
    if player == 1:
        choice = Fore.LIGHTBLACK_EX + "Rock"
    elif player == 2:
        choice = Fore.WHITE + "Paper"
    elif player == 3:
        choice = Fore.RED + "Scissors"
    else:
        print(Fore.RED + "Invalid choice\n")
        continue

    print(Fore.GREEN + "You chose: ", choice)

    computer = random.choice([Fore.LIGHTBLACK_EX + "Rock", Fore.WHITE + "Paper", Fore.RED + "Scissors"])
    print(Fore.MAGENTA + "Computer chose: ", computer)

    if choice == computer:
        print(Fore.YELLOW + "Tie")
    elif choice == "Rock" and computer == "Scissors":
        print(Fore.GREEN + "Player wins")
    elif choice == "Paper" and computer == "Rock":
        print(Fore.GREEN + "Player wins")
    elif choice == "Scissors" and computer == "Paper":
        print(Fore.GREEN + "Player wins")
    else:
        print(Fore.RED + "Computer wins")

    play_again = input(Fore.BLUE + "\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        break
