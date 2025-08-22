import random

print("WELCOME TO ROCK,PAPER,SCISSORS GAME 🗞️✂️🪨")
c = 0
score = 0  # user score
c_score = 0  # computer score
final = True
while final:
    user_choice = int(input("enter your choice : type 0 for rock,1 for paper,2 for scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("your choice is invalid,you lose..😒")
    else:
        computer_choice = random.randint(0, 2)
        print(f"computer choice:{computer_choice}")
        if computer_choice == user_choice:
            print("It is a Draw👍 ")
        elif computer_choice == 0 and user_choice == 2:
            print("you lose.😒")
            c_score += 1
        elif computer_choice == 2 and user_choice == 0:
            print("you win🏆😊")
            score += 1
        elif computer_choice > user_choice:
            print("you loss.😒")
            c_score += 1
        elif computer_choice < user_choice:
            print("you win 🏆😊")
            score += 1
        cont = input("you want to continue is yes type:y else n:\n").lower()
        if cont == "y":
            final = True
        else:

            final = False
    c += 1

print("Result:")
if score > c_score:
    print("you win 🏆😍")
elif score == c_score:
    print("O....It is draw😂")
else:
    print("O..You loss😒.better luck for next time.👍")
print(f"your score is :{score}/{c}\ncomputer score is :{c_score}/{c}")


