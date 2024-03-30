'''
    This is for the Deck class
    
    Attributes (vars) - things it has:
        * list of cards
            
    Methods (fns) - things it does:
        * init - create all the cards in the deck
        * shuffle
        * deal one card
'''

import random
from card import Card
SUITS = ["clubs", "diamonds", "hearts", "spades"]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(len(SUITS)):
                c = Card(i, SUITS[j])
                self.cards.append(c)
                
    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, len(self.cards) - 1)
            # Swap the card at pos r with card at pos i
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        
    def deal(self):
        return self.cards.pop()