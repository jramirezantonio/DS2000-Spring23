'''
    Josue Antonio
    DS 2001 - 2/9/2023
    project1.py
'''
import matplotlib.pyplot as plt
WC_POINTS_TABLE = "Fifa World Cup Points Table.csv"

def main():
    teams = []
    wins = []
    draws = []
    losses = []
    groups = []
    points = []
    goals_for = []
    with open(WC_POINTS_TABLE, "r") as infile:
        while True:
            line = infile.readline().strip().split(",")
        
            if line == [""]:
                break
            
            teams.append(line[1])
            wins.append(line[3])
            draws.append(line[4])
            losses.append(line[5])
            
            goals_for.append(line[6])
            
            points.append(line[9])
            groups.append(line[10])
            
            
    # Want to know which group had the most goals for
    
    goals = goals_for[1:]
    #print(goals)
    
    counter = 0
    group = 0
    sum_goals = 0
    group_goals = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for goal in goals:
        sum_goals += int(goal)
        group_goals[group] = sum_goals
        counter += 1
        
        
        if counter == 4:
            counter = 0
            sum_goals = 0
            group += 1
            
    #print(group_goals)
    #print(groups)
    print("The group with the most goals for had", max(group_goals), "goals, and it was group E.")
    plt.figure(figsize=(16,8))
    plt.bar("A", group_goals[0], color = "deepskyblue")
    plt.bar("B", group_goals[1], color = "red")
    plt.bar("C", group_goals[2], color = "lime")
    plt.bar("D", group_goals[3], color = "gold")
    plt.bar("E", group_goals[4], color = "magenta")
    
    #How to make 1 bar with multiple subbars in it that add up to the E bar
    plt.bar("E (Japan)", 4, color = "silver")
    plt.bar("E (Spain)", 9, color = "salmon")
    plt.bar("E (Germany", 6, color = "peru")
    plt.bar("E (Costa Rica)", 3, color = "blue")
    
    plt.bar("F", group_goals[5], color = "darkviolet")
    plt.bar("G", group_goals[6], color = "aqua")
    plt.bar("H", group_goals[7], color = "darkorange" )
    #print(goals[16:20])
    #print(teams[17:21])
    
    
    #plt.bar("All groups",sum(group_goals))
    plt.title("Total Number of Goals for in each Group")
    plt.xlabel("Groups")
    plt.ylabel("Total Goals")
    plt.ylim(2, 23)
        
  
    
    
    
    
    
main()