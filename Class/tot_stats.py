'''
    DS 2000
    1/27 - Spring 2023
    Smaple code frokm class - tottenham's record so far
    
    How many matches have we won so far this season
    
'''

SOCCER_FILE = "tottenham_results.txt"
import matplotlib.pyplot as plt


def main():
    # Gather data - initialize win count and read from file
    wins = 0
    with open (SOCCER_FILE, "r") as infile:
        while True:
            opponent = infile.readline()
            tot_score = infile.readline()
            opp_score = infile.readline()
            
            
            # If we're at the end of file, stop
            if opponent == "":
                break
            
            
            # Data must be valid to get here!
            tot_score = int(tot_score)
            opp_score = int(opp_score)
            
            print(tot_score, ":", opp_score)
            
            # If we won, update the wins
            if tot_score > opp_score:
                wins += 1
    
    # Communication - how many have we won so far?
    print("Wins:", wins)
    
    # Commuication - show njumber of wins in a bar chart
    plt.bar(1, wins)
    plt.xlim(0, 2)
    
    
    
    
main()