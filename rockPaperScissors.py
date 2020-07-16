import random

# winner_alert = print(f'\t\t\t\t\t\tYou win!\n')
# loser_alert = print(f'\t\t\t\t\t\tYou lose\n')
# tie_alert = print(f'\t\t\t\t\t\tTie\n')

# =============== Computer Opponent ===============
possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)
print(f'\n\n\t\t\t\t***{programs_choice}')


# =============== User Choice ===============
users_choice = input(f"\t\t\t\t***Choose rock, paper or scissors: ")
print(f'\t\t\t\t***{users_choice}')


# =============== Rock, Paper, Scissors logic ===============
if users_choice == "rock":
    if programs_choice == "rock":
        print(f'\t\t\t\t\t\tTie\n')
    elif programs_choice == "paper":
        print(f'\t\t\t\t\t\tYou lose\n')
    elif programs_choice == "scissors":
        print(f'\t\t\t\t\t\tYou win!\n')
elif users_choice == "paper":
    if programs_choice == "rock":
        print(f'\t\t\t\t\t\tYou win!\n')
    elif programs_choice == "paper":
        print(f'\t\t\t\t\t\tTie\n')
    elif programs_choice == "scissors":
        print(f'\t\t\t\t\t\tYou lose\n')
elif users_choice == "scissors":
    if programs_choice == "rock":
        print(f'\t\t\t\t\t\tYou lose\n')
    elif programs_choice == "paper":
        print(f'\t\t\t\t\t\tYou win!\n')
    elif programs_choice == "scissors":
        print(f'\t\t\t\t\t\tTie\n') 
else:
    print(f'\t\t\t\t\t\tSure Buddy\n') 