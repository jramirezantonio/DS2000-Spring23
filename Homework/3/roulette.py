'''
     Josue Antonio
     DS 2000
     Homework 3 - Problem 3
     1/30/2023
     roulette.py

'''

import matplotlib.pyplot as plt
import random

STOPPING_THRESHOLD = 50000
KAYLA_PAYOUT = 5
LANEY_PAYOUT = 50

def main():
    # Gather Data - initialize variables, generate random roulette number
    kayla_money = 0
    kayla_wins = 0
    laney_money= 0
    laney_wins= 0
    
    # Roulette game simulation runs until either Kayla or Laney wins $50000
    while kayla_money < STOPPING_THRESHOLD and \
                                            laney_money < STOPPING_THRESHOLD:
        roulette_number = random.randint(0, 36)
        
        # Give Kayla and Laney their earnings if they bet correctly
        if roulette_number % 2 == 1:
            kayla_money += KAYLA_PAYOUT
            kayla_wins += 1
            if roulette_number == 31:
                laney_money += LANEY_PAYOUT
                laney_wins += 1
        elif roulette_number == 32:
            laney_money += LANEY_PAYOUT
            laney_wins += 1
    
    
    # Communication - create bar chart of number of player's wins, set 
    # appropriate x-limit, add title, and labels
    plt.bar(1, kayla_wins)
    plt.bar(2, laney_wins)
    plt.xlim(0, 3)
    plt.ylabel("Number of wins")
    plt.xlabel("Players")
    plt.title("Number of Kayla wins vs. Number of Laney wins")
    plt.xticks([1, 2], ["Kayla", "Laney"])
    plt.show()
    
    # Communication - create bar chart of total player's earnings, set 
    # appropriate x-limit, add title, and labels
    plt.bar(1, kayla_money)
    plt.bar(2, laney_money)
    plt.xlim(0, 3)
    plt.ylabel("Money won")
    plt.xlabel("Players")
    plt.title("Kayla's earnings vs. Laney's earnings")
    plt.xticks([1, 2], ["Kayla", "Laney"])

main()