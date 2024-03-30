'''
    Josue Hafid
    Spring 2023
    Sample code from class - using lists to look at tottenham results
    Iterating by value, and by position
    
    (Same file from Friday)
'''

TOTTENHAM_FILE = "tottenham_results.txt"

def main():
    # Gather data - read from th efile using a while loop
    # Store data for opponents, tot scores, opp scores in lists
    opponents = []
    tot_scores = []
    opp_scores = []
    with open (TOTTENHAM_FILE, "r") as infile:
        while True:
            opponent = infile.readline()
            tot_score = infile.readline()
            opp_score = infile.readline()
            
            if opponent == "":
                break
            
            # If I get this far, then I have legit data for one match
            opponents.append(opponent.strip())
            tot_scores.append(int(tot_score))            
            opp_scores.append(int(opp_score))
            
    
    # Computation - explore the lists
    for opp in opponents:
        if opp == "Arsenal":
            print("BOOOO")
        else:
            print(opp)
        
    close_wins = 0
    for i in range(len(tot_scores)):
        if tot_scores[i] == 1 and tot_scores[i] > opp_scores[i]:
            close_wins += 1
            
    for i in range(len(tot_scores)):
        tot_scores[i] += 1        
            
            
    # Communication
    print("\nClose wins:", close_wins)
    
    # How many total goals in the most recent 3 matches
    recent_tot_goals = tot_scores[0] + tot_scores[1] + tot_scores[2]
    recent_opp_goals = opp_scores[0] + opp_scores[1] + opp_scores[2]
    print("In the last three games, the hotspurs have scored", 
          recent_tot_goals)
    print("In the last three games, our opponents have scored", 
          recent_opp_goals)
    
    # Who have we played so far this season?
    # Use a for loop to look at everything in the list, one at a time
    # inside the loop, opp just like any other variable
    for opp in opponents:
        print(opp)
    
    # How many games have we played this season?
    games = len(opponents)
    print("We've played", games, "games so far!")
    
main()