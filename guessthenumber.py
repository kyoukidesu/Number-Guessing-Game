import time
from random import randint


welcome_msg = """
Are you ready to guess a number?
I'm thinking of a number between 0 and 100.
You have 5 chances to guess the correct number, sounds fair?
"""

print(welcome_msg)
time.sleep(0.5)

def main():

    diff_text = "Easy: 10 chances\nMedium: 5 chances\nHard: 3 chances\n"
    time.sleep(0.5)
    print(diff_text)

    diff = input("Select your difficulty: ")
    chances = 0

    while diff != "Easy" and diff != "Medium" and diff != "Hard":
        diff = input("Please select the given difficulties: ")

    if diff == "Easy":
        chances = 10
    elif diff == "Medium":
        chances = 5
    elif diff == "Hard":
        chances = 3

    rand_num = randint(0, 100)

    while chances > 0:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Insert a number!")
            continue

        if guess == rand_num:
            print("Spot on!")
            play_again = input("Do you want to play again? (Y/N) ")
            if play_again == "Y":
                main()
            elif play_again == "N":
                print("Goodbye!")
                time.sleep(1.5)
                exit()
            while play_again != "Y" and play_again != "N":
                play_again = input("Choose Y (Yes) or N (No) (Y/N) ")
        elif guess < rand_num:
            print("Too low!")
            chances -= 1
        else:
            print("Too high!")
            chances -= 1

    if chances == 0:
        another_round = input("Game over! Wanna try again? (Y/N) ")
        if another_round == "Y":
            main()
        elif another_round == "N":
            print("Goodbye!")
            time.sleep(1.5)
            exit()
        while another_round != "Y" and another_round != "N":
            another_round = input("Choose Y (Yes) or N (No) (Y/N) ")

main()
