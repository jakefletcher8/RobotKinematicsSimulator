# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:48:55 2026

@author: jakef
"""

#Custom vector class used to handle robot kinematics

class vector():
    def __init__(self,x,y,z):
        
        #Store cartesian x,y and z co-ordinates
        
        self.x = x
        self.y = y
        self.z = z
        
    #Print the current values in the vector
        
    def print_vector(self):
        
        print("X - ", self.x, ", Y - ", self.y, ", Z - ", self.z)
        
        