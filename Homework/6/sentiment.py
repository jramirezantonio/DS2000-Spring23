'''
    Josue Antonio
    DS 2000
    Homework 6 Problem 1
    3/19 - Spring 2023
    sentiment.py
'''

import matplotlib.pyplot as plt

NEUCOMMENTS = "reddit.txt"
SENT_WORDS = {"lenient" : .4, "best" : 1, "unique" : .5, "fulfilling" : .6, 
              "ridiculousness" : -.5, "ridiculous" : -.5, 
              "discrimination" : -1, "racism" : -1, "opportunities" : .7,
              "recommend" : .7, "slapped" : -.6, "great" : 0.5,
              "highly" : .7, "scam" : -.7, "bomb" : -.9, "climb" : .4,
              "expensive" : -.5, "friends" : .5, "love" : 1,
              "awesome" : .8, "benefits" : .4, "overpower" : .5,
              "stressful" : -.4, "fun" : .3, "sucks" : -.4, "friends" : .5,
              "impossible" : -.6, "miserable" : -.8, "regret" : -.5}

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
        Param: filename string
        Returns: 2d list containing every line of the file
        Does: reads every line of file, removes new line at the
              end of each line, turns all the text to lowercase, 
              and stores all lines in 2d list
    '''
    comments = []
    with open(filename, encoding="utf8") as infile:
        for line in infile:
            line = line.lower().strip().split()
            comments.append(line)
    return comments
                    
def remove_non_alphabets(lst):
    ''' Fn: remove_non_alphabets
        Param: list of words
        Returns: list containing only alphabetical values
        Does: iterates through every character of each word in list and checks
              if char is alphabetical. If so, then a word is constructed char 
              by char and it's stored in list
    '''
    new_lst = []
    alpha_word = ""
    for elt in lst:
        for char in elt:
            if char.isalpha() == True:  
                alpha_word += char
        new_lst.append(alpha_word)
        alpha_word = ""
    return new_lst                 
            
def remove_empty_elts(lst):
    ''' Fn: remove_empty_elts
        Param: list
        Returns: no return
        Does: removes elements of list that have length = 0 (i.e., empty elts)
    '''
    for elt in lst:
        if len(elt) == 0:
            lst.remove(elt)
        
def main():
    # Gather data - get data as 2d list containing each reddit comment
    data = read_txt(NEUCOMMENTS)
    # Removes non alphabetical elts from data and adds only the words to
    # alphabets list
    alphabets = []
    for sentence in data:
        alphabets.append(remove_non_alphabets(sentence))
    # Removes empty string elements from alphabets
    for sentence in alphabets:
        remove_empty_elts(sentence)
    # Sorts list of comments old-to-new instead of new-to-old
    rev_alphabets = alphabets[::-1]
    
    # Computation - get sentiment score (-1 to 1) for each sentence
    scores = []
    for sentences in rev_alphabets:
        score = sentiment_score(sentences, SENT_WORDS)
        scores.append(score)
        
    # Communication - plot sentiment score of each sentence vs. their
    # positions in sentences list

    color, label, label1, label2, label3 = "", ["", "", ""], False, False, \
                                                                    False
    # Color positive, negative, and neutral scores differently, add labels
    # to the first instance of each type of score
    for i in range(len(scores)):
        if scores[i] > 0:
            color = "green"
            if label1 == False:
                label[0] = "positive score"
                label1 = True
                plt.scatter(i, scores[i], color = color, label = label[0])
        elif scores[i] < 0:
            color = "red"
            if label2 == False:
                label[1] = "negative score"
                label2 = True
                plt.scatter(i, scores[i], color = color, label = label[1])
        else:
            color = "orange"
            if label3 == False:
                label[2] = "neutral score"
                label3 = True
                plt.scatter(i, scores[i], color = color, label = label[2])
        plt.scatter(i, scores[i], color = color, s = 18)
        
    # Plot legend, add x,y lims, x,y labels, and a title
    plt.legend()
    plt.ylim(-.05, .33)
    plt.title("NEU Sentiment Scores")
    plt.ylabel("Score")
    plt.xlabel("Comment's position") 
main()
                
            
            

