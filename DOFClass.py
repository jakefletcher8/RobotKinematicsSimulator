# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:08:29 2026

@author: jakef

Class used to store vectors in it's own class, this class will allow for
nodes to be connected to the ends of nodes to allow for more degrees of freedom

TO DO:
    
    -Add some way to add extra degrees of freedom to end of a current DOF
    -Make function to return array recursive to allow for all DOF to be returned
    -Implement 'arms' to have strict joints and rigidity

"""
import rotationFunctions as rF
import numpy as np

class Joint():
    def __init__(self,x,y,z):
        
    #Have the degree of freedom store it's rotation around x, y and z axis
        
        self.x = x
        self.y = y
        self.z = z

        print("Joint Created")
        
        
    def print_Joint(self):
        
        print("X - ", self.x, ", Y - ",self.y, ", Z - ", self.z)
        
        
    def change_rotation(self, axis, rotation):
        
        if ((axis == 'x') or (axis == 'X')):
            
            self.x = self.x + rotation
            
        elif ((axis == 'y') or (axis == 'Y')):
            
            self.y = self.y + rotation
            
        elif ((axis == 'z') or (axis == 'Z')):
            
            self.z = self.z + rotation
        
        else: 
            
            print("Invalid axis, please try again")
            
        
    def reset_rotations(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        
    