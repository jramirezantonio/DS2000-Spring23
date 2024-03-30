'''
    DS 2000
    Spring 2023
    Sample code from class - driver creating card objets
    
    Play go-fish:
        * 2 players
        * dea; 5 cards each
        * get one point for having a pair (same number)
        * one player can ask the other for a card( based on a number)
        * if they hand it over, that's a point
        * otherwise, the player draws from the deck'
    
'''

# From [filename] import [classname]
from card import Card
from deck import Deck

def main():
    # Initialize players
    p1, p2 = 0, 0
    
    # Make a deck and shuffle it
    d = Deck()
    d.shuffle()
    
    # Give each player 5 cards
    p1_cards, p2_cards = [], []
    for i in range(5):
        p1_cards.append(d.deal())
        p2_cards.append(d.deal())
        
    for i in range(2):
        for card in p1_cards:
            print(card)
            
        # Does p1 have have any pairs
        loc1 = -1
        for i in range(len(p1_cards)):
            for j in range(i + 1, len(p1_cards)):
                if p1_cards[i].number == p1_cards[j].number:
                    print("found a pair!")
                    p1 += 1
                    loc1, loc2 = i, j
        if loc1 > -1:
            p1_cards.pop(loc1)
            p1_cards.pop(loc2 - 1)
                    
        # Print points so far
        print("P1 points:", p1)
        
        # go fish!
        print("\n\nGo fish!")
        input("Round over! OK?\n")
        p1_cards.append(d.deal())
        
    for k in range(2):
        for card in p2_cards:
            print(card)
            
        # Does p1 have have any pairs
        loc1 = -1
        for i in range(len(p2_cards)):
            for j in range(i + 1, len(p2_cards)):
                if p2_cards[i].number == p2_cards[j].number:
                    print("found a pair!")
                    p2 += 1
                    loc1, loc2 = i, j
        if loc1 > -1:
            p2_cards.pop(loc1)
            p2_cards.pop(loc2 - 1)
                    
        # Print points so far
        print("P2 points:", p2)
        
        # go fish!
        print("\n\nGo fish!")
        input("Round over! OK?\n")
        p2_cards.append(d.deal())
        
    print("P1 ended with...", p1)
    print("P2 ended with...", p2)
main()
