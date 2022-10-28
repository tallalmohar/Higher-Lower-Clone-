# imported modules/files
import random
import higherlowerart
from higherlowergamedata import data
import sys, subprocess


logo = higherlowerart.logo # logo
versus = higherlowerart.vs
#compare follower function
def compare_followers(celeb1,celeb2, user_answer):
    true_answer = ""
    if celeb1 > celeb2:
        true_answer = "A"
    elif celeb1 < celeb2:
        true_answer = "B"

    if true_answer == user_answer:
        return 0
    else:
        return 1


#score/constant values
score = 0
continue_game = True

print(logo)

while continue_game is True:

    # two random celebs to compare
    random_celeb1 = random.choice(data)
    random_celeb2 = random.choice(data)

    print(f'Compare A: {random_celeb1["name"]}, {random_celeb1["description"]}, from {random_celeb1["country"]}')
    print(versus)
    print(f'Against B: {random_celeb2["name"]}, {random_celeb2["description"]}, from {random_celeb2["country"]}')

    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    checking_answer = compare_followers(random_celeb1["follower_count"], random_celeb2["follower_count"],user_choice.upper())
    if checking_answer == 1:
        subprocess.run('clear')
        print(f'Sorry you are wrong.Final score: {score}')
        continue_game = False

    elif checking_answer == 0:
        score += 1
        print(f"You're right! Current Score: {score}")
    subprocess.run('clear')