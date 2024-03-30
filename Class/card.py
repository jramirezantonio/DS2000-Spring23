'''
    DS 2000
    Spring 2023
    Sample code from class - classes & objects
    Goal - be able to play any card game
    Thinking in an object oriented way, I start by designing the cards.
    
    Save in a file with the same name as the class (card.py)
        * Every class in its own .py file
    
    Card class - 
    attributes (variables): what does it have
        * number
        * suit
        * color
    
    methods (functions): what does it do?
        * init method needs to be there
        *
'''

class Card:
    def __init__(self, value, suit, color = "red"):
        self.number = value
        self.suit = suit
        self.color = color
        
    def __str__(self):
        return str(self.number) + " of " + self.suit
        
    

