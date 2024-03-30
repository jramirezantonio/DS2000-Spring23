'''
    DS2000
    Spring 2023
    Sample code from class - reading from a file with a new structure 
    and getting practice with:
        1. slicing
        2. plotting lists
        3. range
        4. list comprehension
        
        
'''
RUNNER_FILE = "laney_garmin.txt"

def main():
    # Gather data - read in data from the file
    # File has multiple values in one line
    with open(RUNNER_FILE, "r") as infile:
        runner_data = infile.readline()
        
        # Turn my big string into a list of strings
        runner_data = runner_data.split()
        
        # Slicing - how do I create a list with everything except my name?
        # This will slice from position 2 to the end of the list
        run_values = runner_data[2:]
        
        # Save the name by itself
        runner_name = runner_data[0] + " " + runner_data[1]
        print(runner_name)
        
        # Range - how do I grab every other value, so that I have a list of
        # distances?
        distances = []
        for i in range(1, len(run_values), 2):
            distances.append(run_values[i])
            
        # List Comprehension - turn list of strings into list of floats
        distances = [float(num) for num in distances]
        
        
        
    
    
    
    
    
    
    
main()
