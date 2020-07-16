"""
Dummy file to challenge and test regular expressions in Python
"""
from math import sqrt #this imports squareroot
import numpy as np  #import numpy as np
 import sys  #this imports sys
notimport = "error"

class Cell: #class Celle: is used to define the class celle
    # Constructor
    def __init__(self): #this says def __init__(self)
        self.status = "p" +"dead" + "a"
        self.alive = False
        try:
            self.alivetext = "False"
        except:
            self.import = "import math"

    # Change status to dead
    def settDead(self): #       def test(self, input): # def # def test():
        self.status = "dead" + status + "1" #contains "dead"

    #Change status to alive
    def settAlive(self):
        self.status = "alive"

    #Get status
    def isAlive(self):
        if self.status == "alive":
            return True #this is return True
        else:
            return False #False False

    #Gets statsus represented by "0" or "."
    def getStatusSymbol(self):
        if self.status == "alive":
            return "O"
        else:
            return "."

#testing colors on loops
for a in "b":
    while a(b) == true:
        print(" ")
