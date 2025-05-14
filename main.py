import random
from game_data import data
from art import logo
from art import vs

score = 0
winner = ""
guess = True
status = True

print(logo)
option_B = random.choice(data)

while status:

    print(f'Current Score: {score}')

    option_A = option_B
    option_B = random.choice(data)

    # Guess Input
    guess = input(f"Compare A: {option_A['name']},"
                f"a {option_A['description']},"
                f"from {option_A['country']}"
                f"{vs} \n"
                f"Against B: {option_B['name']},"
                f"a {option_B['description']},"
                f"from {option_B['country']}.\n"
                f"\nWho has more followers? "
                f"\nType \'A\' or \'B\':")

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Select Winner:
    if option_A['follower_count'] > option_B['follower_count']:
        winner = "A"
    elif option_B['follower_count'] == option_A['follower_count']:
        print('even')
    else:
        winner = "B"

    # Increase Score:
    if guess == winner:
        score += 1

    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        status = False










