'''
    Josue Antonio
    DS 2000
    Spring 2023
    Sample code from class - 
        - reading CSV files
        - writing our own max/min algorithm
        - plotting lists
        - looking for runner who ran the most
    
'''
import matplotlib.pyplot as plt
RUNNER_FILE = "runner_data.csv"
NAME_POS = 0

def main():
    # Initialize max mileage seen so far
    max_mileage = 0
    max_runner = ""
    
    # Gather Data - read in runners from CSV file
    with open(RUNNER_FILE, "r") as infile:
        # Read in and save the dates (first line)
        dates = infile.readline().split(",")
        dates = [int(date) for date in dates]
        
        # Read in every runner's data
        for line in infile:
            
            # Turn the current line (string) into a list
            lst = line.split(",")
            
            # Pull out the current runner's name
            name = lst[NAME_POS]
            runner_data = lst[NAME_POS+1:]
            # Or use pop(index) which removes the iteam at the given index
            
            #print(runner_data)
            
            # Turn the runner's data into floats (use list comprehension)
            runner_data = [float(num) for num in runner_data]
            
            # Is this mileage the new maximum?
            current_mileage = sum(runner_data)
            if current_mileage > max_mileage:
                max_mileage = current_mileage
                max_runner = name
                
            # Plot the current runner against the dates
            plt.scatter(dates, runner_data, label = name)
            
    # Communication - what was the max mileage seen in the file?
    print("The max mileage in January was:", max_mileage, "which was ran by",
          max_runner)
    plt.legend()
            
    
main()