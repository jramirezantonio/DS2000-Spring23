'''
    Josue Antonio
    DS 2000
    Homework 7 Problem 1
    3/28 - Spring 2023
    runner.py
'''
import matplotlib.pyplot as plt

class Runner:
    ''' Runner class represents one Khoury runner
        
        A runner has: name, xpos, ypos, color, and a runs list containing 
                      the distances the runner ran each day of the month
                      
        init method: create a runner with xpos, ypos, and color as optional
                     if optional attributes not given, we default  to runner
                     in (0, 0) pos with color black
                     
        draw method: render runner on grid at its current xpos, ypos and with 
                     its color
        
        add_run method: append given run (float) to the runner's list of runs
        
        get_total_distance method: return total distance of all runs in 
                                   runner's list of runs
        
        move_next method: update runners current xpos to next position in 
                          runner's list of runs
        
        str method: print the name and the color of the runner
    '''
    def __init__(self, name, x = 0, y = 0, color = "black"):
        self.runs = []
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self):
        plt.plot(self.x, self.y, color = self.color, marker = ">", 
                                     markersize = 10, label = self.name)
    
    def add_run(self, run):
        self.runs.append(float(run))
        
    def get_total_distance(self):
        return sum(self.runs)
    
    def move_next(self):
        if len(self.runs) != 0:
            self.x += self.runs.pop(0)
        
    def __str__(self):
        return str(self.name + " the " + self.color + " runner!")