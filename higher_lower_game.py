import random
from data import celebs
import art
import os

score=0
game_over=False
repeat=True

account_A=random.choice(celebs)

celeb_A=account_A["name"]
followers_A=account_A["follower_count"]
description_A=account_A["description"]
country_A=account_A["country"]

while repeat!=False:

    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(art.logo)
    print(f"\nScore: {score}")
    celeb_A=account_A["name"]
    followers_A=account_A["follower_count"]
    description_A=account_A["description"]
    country_A=account_A["country"]
    print(f"\nCompare A: {celeb_A}, a {description_A} from {country_A}")

    # print(art.vs)

    account_B=random.choice(celebs)

    if account_A==account_B:
        account_B=random.choice(celebs)

    celeb_B=account_B["name"]
    followers_B=account_B["follower_count"]
    description_B=account_B["description"]
    country_B=account_B["country"]

    print(f"\nAgainst B: {celeb_B}, a {description_B} from {country_B}")


    answer=input("\nWho has more followers? Type 'A' or 'B': ").lower()

    if answer=='a':

        if followers_A>followers_B:
            score+=1
            account_A=account_B

        elif followers_B>followers_A:
            print("\nYou're wrong, try again next time :')")
            score=0
            
            new_game=input("\nWanna play another game? Type 'yes' or 'no': ").lower()
            
            if new_game=='yes':
                continue
            elif new_game=='no':
                repeat=False
            else:
                print("Invalid Input, exitting.....")

    elif answer=='b':

        if followers_A>followers_B:
            print("\nYou're wrong, try again next time :')")
            score=0

            new_game=input("\nWanna play another game? Type 'yes' or 'no': ").lower()
            
            if new_game=='yes':
                continue
            elif new_game=='no':
                repeat=False
            else:
                print("Invalid Input, exitting.....")
                repeat=False

        elif followers_B>followers_A:
            score+=1
            account_A=account_B
            


