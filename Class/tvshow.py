'''
    DS2000
    Spring 2023 
    Sample code from class to make TV show recommendations
    
    This class is a combo of user/show attributes:
        * Name of show
        * popoularity (1-10)
        * length (# of minutes per ep, on average)
        * individual rating (1-10)
        
    Methods:
        * __init__
        * ...
    Algorithm:
        * create a bunch of TVShow objects
        * then, ask the user about a show they've recently watched
        * recommend from a list of TVShow objects, shows with similar length, 
          popoularity, and a good rating
'''

MIN_RATING = 6
LOW_POP = 5
LENGTH_SIM = 5 

class TVShow:
    def __init__(self, title, pop = 1, length = 30, rating = 1):
        self.title = title
        self.pop = pop
        self.length = length
        self.rating = rating
        
    def recommend(self, other): # other is convention when using other obj
        if self.rating >= MIN_RATING:
            if other.pop <= LOW_POP  and self.pop <= LOW_POP \
            or other.pop > LOW_POP and self.pop > LOW_POP:
                if abs(self.length - other.length) <= LENGTH_SIM:
                    return True
        return False
                    
    def __str__(self):
        return self.title + " with rating " + str(self.rating)
    
    def euclidean(self, other):
        distance = (self.length - other.length) ** 2 + \
        (self.pop - other.pop) ** 2 + (self.rating - other.rating) ** 2
        return distance ** 0.5