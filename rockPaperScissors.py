import random

# =============== Message variables ===============
# winner_alert = print(f'\t\t\t\t\t\tYou win!\n')
# loser_alert = print(f'\t\t\t\t\t\tYou lose\n')
# tie_alert = print(f'\t\t\t\t\t\tTie\n')

# =============== Message variables ===============
score = {
    "wins": 0,
    "loses": 0,
    "ties": 0
}

# =============== Computer Opponent ===============
possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)
print(f'\n\n\t\t\t\t***{programs_choice}')


# =============== User Choice ===============
users_choice = input(f"\t\t\t\t***Choose rock, paper or scissors: ")
print(f'\t\t\t\t***{users_choice}\n')

# =============== Rock, Paper, Scissors logic ===============
if users_choice == "rock":
    if programs_choice == "rock":
        score["ties"] += 1
        print(f'\t\t\t\t\t\tTie\n')
    elif programs_choice == "paper":
        score["loses"] += 1
        print(f'\t\t\t\t\t\tYou lose\n')
    elif programs_choice == "scissors":
        score["wins"] += 1
        print(f'\t\t\t\t\t\tYou win!\n')
elif users_choice == "paper":
    if programs_choice == "rock":
        score["wins"] += 1
        print(f'\t\t\t\t\t\tYou win!\n')
    elif programs_choice == "paper":
        score["ties"] += 1
        print(f'\t\t\t\t\t\tTie\n')
    elif programs_choice == "scissors":
        score["loses"] += 1
        print(f'\t\t\t\t\t\tYou lose\n')
elif users_choice == "scissors":
    if programs_choice == "rock":
        score["loses"] += 1
        print(f'\t\t\t\t\t\tYou lose\n')
    elif programs_choice == "paper":
        score["wins"] += 1
        print(f'\t\t\t\t\t\tYou win!\n')
    elif programs_choice == "scissors":
        score["ties"] += 1
        print(f'\t\t\t\t\t\tTie\n') 
else:
    print(f'\t\t\t\t\t\tSure Buddy')

print(f'\t\t\t\tYour SCORE = {score}\n\n\n\n')