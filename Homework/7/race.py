'''
    Josue Antonio
    DS 2000
    Homework 7 Problem 2
    3/28 - Spring 2023
    race.py
'''
import matplotlib.pyplot as plt
from runner import Runner

RUNNERS_DATA = "runner_data.txt"

def read_txt(filename):
    ''' Fn: read_txt
        Param: string (filename)
        Returns: list, list tuple
        Does: reads every line of file, removes new line at end of each line,
              stores first line in header lst, and all other lines in data lst
    '''
    data = []
    with open(filename, "r") as infile:
        header = infile.readline().strip().split()
        for line in infile:
            data.append(line.strip().split())
    return data, header

def create_runners(data):
    ''' Fn: create_runners
        Param: data (list)
        Returns: runners list
        Does: instantiates runner for each line of given data, saves each
              runner's data in runners list, including the distances they ran
        '''
    runners = []
    for line in data:
        name = line[0]
        runner = Runner(name)
        runners.append(runner)
        runners_values = line[2:]
        for dist in runners_values:
            runner.add_run(dist)
    return runners

def max_distance(runners):
    ''' Fn: max_distance
        Param: list of runner objects
        Returns: float, int tuple
        Does: computes max total distance ran by any runner in given 
              list and its pos in list 
    '''
    max_dist, max_runner_pos = 0, 0
    for runner in runners:
        runner_tot_dist = runner.get_total_distance()
        if runner_tot_dist > max_dist:
            max_dist = runner_tot_dist
            max_runner_pos = runners.index(runner)
    return max_dist, max_runner_pos

def plot_daily_runners(runners, days, colors, month):
    ''' Fn: plot_daily_runners
        Param: list of runners, list of days in month, list of colors,
               and month (string)
        Returns: nothing 
        Does: calls max_dist fn, sets y pos for each runner in runners list,
              sets color for each runner using provided list, for each day in 
              provided list, generates a new plot that renders all the
              runners, update their x pos each time with the amt they ran that
              day, and prints out the runner with the max total distance ran
    '''
    ypos = len(runners)
    extra_miles_threshold = 10
    max_dist, max_runner_pos = max_distance(runners)
    for runner in runners:
        runner.y = ypos
        ypos -= 1
    for i in range(len(runners)):
        runners[i].color = colors[i]
    for day in days:
        for runner in runners:
            runner.move_next()
            runner.draw()
        plt.xlim(0, max_dist + extra_miles_threshold)
        plt.ylim(0, extra_miles_threshold)
        plt.title("Khoury Runners - " + month + " Miles")
        plt.xlabel("Miles covered so far")
        plt.legend()
        plt.show()
    print("The winner of the " + month + " race:", runners[max_runner_pos])
            
def main():
    # Gather data - get data as lst, lst tuple contatining all runners data,
    # and header of data
    runners_data, header = read_txt(RUNNERS_DATA)
    # Computation - instantiates runner object for each line in data , and 
    # store each runner's data in runners list
    runners = create_runners(runners_data)  
    # Get max total distance ran by any runner and its position in runners lst
    max_dist, max_runner_pos = max_distance(runners)
    
    # Communication - create list of only days in given month (February)
    # Plot every runner at once for each day of month, print runner who 
    # ran the furthest overall
    header = header[2:]
    header = [int(x) for x in header]
    colors = ["fuchsia", "orange", "purple", "blue", "red"]
    plot_daily_runners(runners, header, colors, "February") 
main()

