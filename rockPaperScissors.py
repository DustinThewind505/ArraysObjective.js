import random

possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)
print(f'\n\n\t\t\t\t***{programs_choice}')

users_choice = input(f"\t\t\t\t***Choose rock, paper or scissors: ")
print(f'\t\t\t\t***{users_choice}\n')

