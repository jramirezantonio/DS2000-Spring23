'''
    Josue Antonio
    DS 2000
    Spring 2023
    Sample code from class - practice with functions
    
    Our own functions are defined above main
'''
import random
import matplotlib.pyplot as plt

def max_list(lst):
    ''' Function: max_list
        Parameters: a list of ints/floats
        Return: int/float
        Does: finds and returns the max value in the list
    '''
    curr_max = -1
    for num in lst:
        if num > curr_max:
            curr_max = num
    return curr_max
    print("This doesn't run")
    
def plot_list(lst):
    ''' Function: plot_list
        Parameters: a list of ints/floats
        Returns: nothing
        Does: makes a line chart
    '''    
    plt.plot(lst)
    plt.title("List of random values")
    plt.xlabel("Position")
    plt.ylabel("Random value"
    mx = max_list(lst)          
    plt.ylim(0, mx + 1)
    
def main():
    for i in range(2):
        # Gather data - generate random lists
        lst = [random.randint(1,10) for i in range(5)]
        
        # Computation - find the max of the list
        max = max_list(lst)
        print(lst)
        print("The max in the list is:", max)
        plot_list(lst)
     
    
main()