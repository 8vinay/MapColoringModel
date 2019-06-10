'''
This file contains a map coloring model that is capable of coloring
the map of Australia.The model attempts to color the states in Australia
such that no two neighboring states have the same color.
'''
import random

'''
The map of Australia can be represented in many ways. Here we represent
it in the form of a dictionary, where each state is a key in the
dictionary and the values correspond to the neighoring states.
'''

#list of states in Australia
WA  = 'western australia'
NT  = 'northern territory'
SA  = 'south australia'
Q   = 'queensland'
NSW = 'new south wales'
V   = 'victoria'
T   = 'tasmania'

#states and their corresponding neighbors
australia = { T:   {},
              WA:  {NT, SA},
              NT:  {WA, Q, SA},
              SA:  {WA, NT, Q, NSW, V},
              Q:   {NT, SA, NSW},
              NSW: {Q, SA, V},
              V:   {SA, NSW, T} }
steps = 0
backcount = 0
utilcount = 0

colors = {'1': 'Red', '2': 'Green', '3': 'Blue'}

#states are assigned colors in this order
states = {0: 'tasmania', 1: 'western australia', 2: 'northern territory', 3:'south australia', 4: 'queensland', 5:'new south wales', 6:'victoria'}

class Map(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.LTM = [[0 for column in range(vertices)] 
                              for row in range(vertices)] 
  
    '''
    This is a function to check if the color assignment doesn't violate the
    constraint that neighboring states shouldn't have the same color. For
    each color chosen by the model, it verifies whether any  of the
    neighboring states has the same color or not. The neighboring
    states are fetched from the long term memory and the color assignment
    is checked in the working memory. 
    '''

    def isSafe(self, v, WM, c): 
        global steps
        global backcount
        steps += 1
        print "assign color",colors.get(str(c), 'default') ,"to",states.get(v, 'default')
        for i in range(self.V): 
            if self.LTM[v][i] == 1 and WM[i] == c:
                backcount += 1 
                return False
        return True
    
    '''
    This is a utility function which assigns colors to the states of the map.
    The color of each state is stored in the working memory as long as it
    doesn't violate the constraint. If it does, the model replaces it with
    a new color.
    '''  
    
    def colorUtility(self, m, WM, v):
        global utilcount
        utilcount += 1 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.isSafe(v, WM, c) == True: 
                WM[v] = c 
                if self.colorUtility(m, WM, v+1) == True: 
                    return True
                WM[v] = 0

    '''
    This is the main function which determines whether a solution is found
    with the given number of colors. It prints the solution i.e. the color
    assigned to each state without violating the map coloring constraint,
    if a solution is found.
    '''

    def mapColoring(self, m):
        global steps
        WM = [0] * self.V 
        if self.colorUtility(m, WM, 0) == False: 
            return False
        
        # Print the solution 
        if 0 in WM:
            print "\nCould not find solution"
        else:
            print "\nFollowing are the assigned colors to the regions:"
            for i,c in zip(self.LTM,WM): 
                print states.get(self.LTM.index(i), 'default'),":",colors.get(str(c), 'default') 
        print "\nNumber of steps:",steps
        steps = 0
        return True

#number of colors
m=3
#number of states
g  = Map(7)

'''
Long term memory is used to store the details of the map. It is stored in
the form of an adjacency matrix. If two states are neighbors, then the
coresponding row and column value will be equal to 1 and it will be equal
to 0 otherwise. 
''' 
g.LTM = [[0,0,0,0,0,0,0], 
           [0,0,1,1,0,0,0],
           [0,1,0,1,1,0,0],
           [0,1,1,0,1,1,1],
           [0,0,1,1,0,1,0],
           [0,0,0,1,1,0,1],
           [0,0,0,1,0,1,0]]

steps = 0
