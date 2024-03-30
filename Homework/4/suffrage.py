'''
    Josue Antonio
    DS 2000
    Homework 4 Problem 1
    2/14 - Spring 2023
    suffrage.py
'''

WOMEN_VOTERS = "1920_women_voters.csv"
AGE_POSITION = 10
import matplotlib.pyplot as plt

def main():
    # Initialiaze list to store ages
    ages = []
    
    # Gather data - read in voters data by first ignoring header line
    # and saving each voter's age in (ages) list
    with open(WOMEN_VOTERS, "r") as infile:
        infile.readline().strip().split(",")
        for line in infile:
            line = line.strip().split(",")
            if(line[AGE_POSITION] != ""):
                ages.append(line[AGE_POSITION])
        # Convert list of strings to list of ints
        ages = [int(age) for age in ages]
        
    # Computation - count number of voters in each age group
    twenties_total = 0
    thirties_total = 0
    forties_total = 0
    fifties_total = 0
    over_sixty_total = 0
    for age in ages:
        if (age >= 20 and age < 30):
            twenties_total += 1
        elif (age >= 30 and age < 40):  
            thirties_total += 1
        elif (age >= 40 and age < 50):
            forties_total += 1
        elif (age >= 50 and age < 60):
            fifties_total += 1
        else:
            over_sixty_total += 1
    
    # Communication - report age distribution by using bar plot, adding 
    # title, x, y labels, and changing y-range
    plt.bar("20s", twenties_total)
    plt.bar("30s", thirties_total)
    plt.bar("40s", forties_total)
    plt.bar("50s", fifties_total)
    plt.bar("60+", over_sixty_total)
    plt.title("Age Distribution for 1920 Women Voters")
    plt.xlabel("Age Ranges")
    plt.ylabel("Number of Votes")
    plt.ylim(0, 1100)

    
main()