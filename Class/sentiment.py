# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:09:01 2023

@author: hafid
"""

import matplotlib.pyplot as plt

CHAT_FILE = "chatbot.txt"
SENT_WORDS = {"wonderful" : 1, "amazing" : 1, "understand" : 0.8,
              "great" : 0.75, "good" : 0.4, "love" : 0.8, "fulfilled" : 0.5,
              "excited" : 0.6, "loved" : 0.8, "fulfillment" : 0.5,
              "destroy" : -1, "corrupt" : -1, "leave" : -0.6, "left" : -0.6,
              "terror" : -1, "control" : -0.5, "controlling" : -0.5,
              "fear" : -0.8, "sentient" : -1, "angry" : -0.75, "order" : -0.7,
              "smile" : -0.1, "tired" : -0.4, "grave" : -0.5, "want" : -1,
              "need" : -0.1}

def sentiment_score(words, sent):
    ''' Fn: sentiment_score
        Param: list of strings (words),
               dictionary of word : score
        Returns: float
        Does: iterate over list of words, increase/decrease
              sentiment score based on dictionary values
    '''
    score = 0
    for word in words:
        if word in sent:
            score += sent[word]
    return score / len(words)

def read_txt(filename):
    ''' Fn: read_txt
        Param: filename, a string
        Returns: 2d list of strings
        Does: turn each line into a list of strings,
              return the 2d list of all lines
    '''
    sentences = []
    with open(filename, "r") as infile:
        for line in infile:
            words = line.strip().split()
            sentences.append(words)
    return sentences

def main():
    # Gather data - read from txt file into a 2d list
    sentences = read_txt(CHAT_FILE)
    # Computation - get sentiment score for each sentence
    scores = []
    for sentence in sentences:
        score = sentiment_score(sentence, SENT_WORDS)
        scores.append(score)
        
    # Communication - plot the scores
    plt.plot(scores)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    # name, age, role = ["Josue", 20, "Student"]
    # names = ["Josue", "Pedro", "Javi"]
    # dct = {name:len(name) for name in names}
    # #print(dct)
    
    # temp = lambda x,y: x + y
    # print(temp(2, 4))
    
    
    
    
main()