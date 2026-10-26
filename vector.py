# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:48:55 2026

@author: jakef
"""

import numpy as np

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
        
        
    #rotate the vector for a given axis and angle
        
    def rotation_matrix(self, axis, angle):
        
        #define degree to radians variable
        
        deg_to_radians = np.pi/180
        
        #if angle is 0 then save computation
        
        if (angle == 0):
            
            return
        
        
        
        elif ((axis == 'x') or (axis == 'X')):
        
            #change values due to rotation matrix    
        
            new_x = self.x
            new_y = self.y*np.cos(angle*deg_to_radians) - self.z*np.sin(angle*deg_to_radians)
            new_z = self.y*np.sin(angle*deg_to_radians) + self.z*np.cos(angle*deg_to_radians)
        
        elif ((axis == 'y') or (axis == 'Y')):
            
            new_x = self.x*np.cos(angle*deg_to_radians) + self.z*np.sin(angle*deg_to_radians)
            new_y = self.y
            new_z = -1*self.x*np.sin(angle*deg_to_radians) + self.z*np.cos(angle*deg_to_radians) 
        
        elif ((axis == 'z') or (axis == 'Z')):
            
            new_x = self.x*np.cos(angle*deg_to_radians) - self.y*np.sin(angle*deg_to_radians)
            new_y = self.x*np.sin(angle*deg_to_radians) + self.y*np.cos(angle*deg_to_radians)
            new_z = self.z 
        
        #round values to remove floating point errors
        
        self.x = round(new_x)
        self.y = round(new_y)
        self.z = round(new_z)