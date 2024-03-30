# -*- coding: utf-8 -*-
'''
    Josue Antonio
    Spring 2023
    Sample code from class - dice rolling simulation - Jan 24th
    
'''

import random

def main():
    # Gather data - rolling two dice, 1-6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    money = 20
    
    # Sanity check - print, did I get legit values?
    print("Die 1:", die1, "\nDie 2:", die2)
    
    # Computation - implement the rules of the dice game
    
    if die1 == 4 or die1 == 6:
        money = money + 10
    
    if die2 == 4 or die2 == 6:
        money = money // 2
        
    if die1 == die2:
        money = money * 2
    elif (die1 + die2) >= 10:
        money = 0
    
        
        
    
    # Communication - report the money I now have
    
    print("After rolling two dice, Laney has $", money, sep = "")
    
    
    
    
    
    
    
main()

