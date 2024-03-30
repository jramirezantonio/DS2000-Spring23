'''
    Josue Antonio
    DS 2000
    Homework 2 Problem 2
    1/23 - Spring 2023
    race.py
    
    Test case:
        Laney's location (3, 4)
        Cooper's location (1, 3)
        Euclidean distance = ((1 - 3) ** 2 + (3 - 4) ** 2) ** (1 / 2) = 2.236
        Time to reach Cooper = 2.236 * 10 = 22 minutes
'''

LOCATIONS = "locations.txt"

def main():
    # Gather data - read in names, and (x, y) coords. of Cooper's fans from
    # text file, and prompt the user for Cooper's (x, y) coords. 
    coopers_xpos = int(input("What's Cooper's x position (1-5)?\n"))
    coopers_ypos = int(input("What's Cooper's y position (1-3)?\n"))
    
    with open(LOCATIONS, "r") as infile:
        name1 = infile.readline().strip()
        x_pos1 = int(infile.readline())
        y_pos1 = int(infile.readline())
        name2 = infile.readline().strip()
        x_pos2 = int(infile.readline())
        y_pos2 = int(infile.readline())
    # Computation - calculate distance between the fans' locations to 
    # Cooper's, and the respective time it'll take each fan to reach him
    distance1 = ((coopers_xpos - x_pos1) ** 2 + (coopers_ypos - y_pos1) ** 2)\
                                                                    ** (1 / 2)
    distance2 = ((coopers_xpos - x_pos2) ** 2 + (coopers_ypos - y_pos2) ** 2)\
                                                                    ** (1 / 2)                                       
    time1 = distance1 * 10
    time2 = distance2 * 10
    
    # Communication - report distances rounded to 3 places and times rounded 
    # to nearest minute
    print(name1, "is", round(distance1, 3), "units away from Cooper and it "\
          "would take", round(time1), "minutes to reach him.\n")
      
    print(name2, "is", round(distance2, 3), "units away from Cooper and it "\
          "would take", round(time2), "minutes to reach him.\n")
    
        
main()



    