from tkinter.font import BOLD
import sys
import random
import tkinter
import os
os.system("")
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

player_score = 0
computer_score = 0



while True:
    print(Fore.LIGHTBLUE_EX + "\n\n     ==============\n     Rock Paper Scissors\n     ==============")
    print(Fore.LIGHTBLACK_EX + "     1. Rock")
    print(Fore.WHITE + "     2. Paper")
    print(Fore.RED + "     3. Scissors")
    print(Fore.LIGHTBLUE_EX + "     ==============\n\n")


    prompt = Fore.LIGHTBLUE_EX + "     Please choose a number between 1-3:\n     (   )\033[3D"
    player = (input(prompt))
    if player == "1":
        choice = "Rock"
    elif player == "2":
        choice = "Paper"
    elif player == "3":
        choice = "Scissors"
    else:
        print(Fore.RED + "\n     Invalid choice\n")
        continue

    player = int(player)

    colors = {"Rock": Fore.LIGHTBLACK_EX, "Paper": Fore.WHITE, "Scissors": Fore.RED}
    print(Fore.LIGHTGREEN_EX + "\n     You chose: ", colors[choice] + choice)

    computer = random.choice(["Rock", "Paper", "Scissors"])
    print(Fore.LIGHTRED_EX + "     Computer chose: ", colors[computer] + computer + "\n\n")

    if choice == computer:
        print(Fore.YELLOW + "     Tie")
    elif choice == "Rock" and computer == "Scissors":
        print(Fore.GREEN + "     Player wins")
        player_score += 1
    elif choice == "Paper" and computer == "Rock":
        print(Fore.GREEN + "     Player wins")
        player_score += 1
    elif choice == "Scissors" and computer == "Paper":
        print(Fore.GREEN + "     Player wins")
        player_score += 1
    else:
        print(Fore.RED + "     Computer wins")
        computer_score += 1
    print(Fore.LIGHTBLUE_EX + "\n\n     ==============")
    print(Fore.LIGHTGREEN_EX + "\n\n\u001b[6m     Player Score: ", player_score)
    print(Fore.LIGHTRED_EX + "\n\u001b[6m     Computer Score: ", computer_score)
    print(Fore.LIGHTBLUE_EX + "\n     ==============")
    while True:
        play_again = input(Fore.LIGHTBLUE_EX + "\n     Do you want to play again? (y/n): \n     ==============\n     (   )\033[3D").strip().lower()
        if play_again in ["y", "n"]:
            break
        print(Fore.RED + "     Please enter 'y' or 'n'")

    if play_again == "n":
        break