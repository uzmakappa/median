# 103 Johnstone UAB Fall 2016
# Your name: Uzma Nur

import random
from turtle import *

    
def drawLine (p,q):
    
    """Using turtle graphics, draw a triangle.

    Params:
        p (float 2-tuple): coordinates for start point of line
        q (float 2-tuple): coordinates for end point of line
    """
    
    up ()
    goto (p)
    down ()
    goto (q)
    up ()


def drawTriangle (r,s,t):
    
    """Using turtle graphics, draw a line.

    Params:
        r (float 2-tuple): coordinates for first vertex of triangle
        s (float 2-tuple): coordinates for second vertex of triangle
        t (float 2-tuple): coordinates for third vertex of triangle
    """
    
    up ()
    goto (r)
    down ()
    goto (s)
    goto (t)
    goto (r)
    up ()



def drawMedian (r,s,t):
    
    """Using turtle graphics, draw the median of a triangle.

    Params:
        r (float 2-tuple): coordinates for vertex of triangle from which median will be drawn
        s (float 2-tuple): coordinates for first vertex of triangle side to which median will be drawn
        t (float 2-tuple): coordinates for second vertex of triangle side to which median will be drawn
    """
    
    u = ((s[0]+t[0])/2, (s[1]+t[1])/2)
    drawLine (r, u)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def allTriMedian (w=300):

    """Using turtle graphics, draw a random triangle and its three medians.

    Params:
        w (int): triangle should fit in the square with corners [+-w, +-w]
    """

    r = (random.randint(-w, w), random.randint(-w, w))
    s = (random.randint(-w, w), random.randint(-w, w))
    t = (random.randint(-w, w), random.randint(-w, w))
    drawTriangle (r,s,t)
    drawMedian (r,s,t)
    drawMedian (s,t,r)
    drawMedian (t,r,s)
    done ()
    speed (0) # keep max speed, to help the TA's grade


# allTriMedian (250)

# IMPORTANT: 
# you may uncomment this line to test
# but submit code with no testing calls, just the function definitions
