'''
    DS2000
    Spring 2023
    Sample code from class - a TVshow with higlight on its Emmy status
    
    Starter code is below so we can jump in during leture on April 7th.

    Note a few code details we hvaen't covered in class before:
        * ternary operator for on-the-fly decision making
        * f string to generate a string
    
    TODO:
        * method to return the category/label of the show so it can be
          used in classification (the driver doesn't necessarily know
          which attribute is the category or how it's used)
        
'''

class EmmyShow:
    ''' This class represents a TVshow.
        
        Attributes:  title (string), did it win an emmy (0/1),
                     violence level (int 1-5), drama level (int 1-5),
                     and funny level (int 1-5)
        
        Methods: init takes in a list with assumed order title, emmy,
                 violence, drama, funny. Title is required, the rest 
                 can be left out.
                 
                 str returns the title of the show and its emmy status
                 
                 euclidean computes the distance between the show 
                 and the given show
                 
                 get_category returns whether show won emmy (1) or not (0)
    '''
    
    def __init__(self, values):
        self.title = values[0] 
        self.emmy = values[1] if len(values) > 1 else False
        self.violence = values[2] if len(values) > 2 else 1
        self.drama = values[3] if len(values) > 3 else 1
        self.funny = values[4] if len(values) > 4 else 1
        
    def __str__(self):
        result = f"{self.title}, which ..."
        result += "HAS an Emmy " if self.emmy else " is Emmy-less :("
        return result
    
    def euclidean(self, other):
        distance = (self.violence - other.violence) ** 2 + \
            (self.funny - other.funny) ** 2 + (self.drama - other.drama) ** 2
        return distance ** .5
    
    def get_category(self):
        return int(self.emmy)