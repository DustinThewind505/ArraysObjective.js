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

while True:
# =============== Computer Opponent ===============
    possible_choices = ["rock", "paper", "scissors"]
    programs_choice = random.choice(possible_choices)



# =============== User Choice ===============
    users_choice = input(f"\n\n\t\t\t\t***Choose rock, paper or scissors: ")
    print(f'\n\t\t\t\t***You: {users_choice}\n') # prints your choice
    print(f'\t\t\t\t***Computer: {programs_choice}') # prints computer's choice

# =============== Rock, Paper, Scissors logic ===============

    if users_choice == "rock":
        if programs_choice == "rock":
            score["ties"] += 1
            print(f'\n\t\t\t\t\t\tTie')
        elif programs_choice == "paper":
            score["loses"] += 1
            print(f'\n\t\t\t\t\t\tYou lose')
        elif programs_choice == "scissors":
            score["wins"] += 1
            print(f'\n\t\t\t\t\t\tYou win!')
    elif users_choice == "paper":
        if programs_choice == "rock":
            score["wins"] += 1
            print(f'\n\t\t\t\t\t\tYou win!')
        elif programs_choice == "paper":
            score["ties"] += 1
            print(f'\n\t\t\t\t\t\tTie')
        elif programs_choice == "scissors":
            score["loses"] += 1
            print(f'\n\t\t\t\t\t\tYou lose')
    elif users_choice == "scissors":
        if programs_choice == "rock":
            score["loses"] += 1
            print(f'\n\t\t\t\t\t\tYou lose')
        elif programs_choice == "paper":
            score["wins"] += 1
            print(f'\n\t\t\t\t\t\tYou win!')
        elif programs_choice == "scissors":
            score["ties"] += 1
            print(f'\n\t\t\t\t\t\tTie') 
    else:
        print(f'\n\t\t\t\t\t\tSure Buddy')
    print(f'\t\t\t\tYour SCORE = {score}\n\n\n\n')