# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:56:33 2026

@author: jakef

Contains functions that handle 3D rotation matrices that can
be used to calculate new positions of vectors given an angle
of rotation for any axis

"""

import numpy as np

def rotationMatrixX(angle): 
   
    '''
    
    Enter an angle in radians and result is a rotation matrix around the x axis
    
    '''
   
    matrix = [[1,0,0],[0,np.cos(angle),-1*np.sin(angle)],[0,np.sin(angle),np.cos(angle)]]
    
    return np.array(matrix)

def rotationMatrixY(angle): 
   
    '''
    
    Enter an angle in radians and result is a rotation matrix around the y axis
    
    '''
   
    matrix = [[np.cos(angle),0,np.sin(angle)],[0,1,0],[-1*np.sin(angle),0,np.cos(angle)]]
    
    return np.array(matrix)

def rotationMatrixZ(angle): 
   
    '''
    
    Enter an angle in radians and result is a rotation matrix around the z axis
    
    '''
   
    matrix = [[np.cos(angle),-1*np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]]
    
    return np.array(matrix)


def addPoints(point1, point2):
    
    '''
    
    Uses two different numpy arrays to sum together and return result
    
    '''
    
    x = point1[0][0] + point2[0][0]
    y = point1[1][0] + point2[1][0]
    z = point1[2][0] + point2[2][0]
    
    return np.array([[x],[y],[z]])


'''

Function to create a transformation matrix given an axis rotation in radians and position to the next frame

'''

def return_Transformation_Matrix(axis, rotation, position):
    
    
    
    
    return
    
    