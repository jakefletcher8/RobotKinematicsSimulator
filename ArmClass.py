# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:22:01 2026

@author: jakef

Arm class to have a defined length and structure to an arm
"""

import DOFClass as DOF
import numpy as np
import vector as vect
import link
import matplotlib.pyplot as mpl

class ArmPart():
    def __init__(self):
        
        #Links are the bits connecting the rotational parts of the robot
        
        self.links = np.array([link.link(1)])
        
        #Joints are the rotational parts of the robot, revolute as of now but prismatic joints should be added
        
        self.joints = np.array([DOF.Joint(0, 0, 0)])
        
        #Store the vector from one node to the next, may save on computation
        
        self.vectors = np.array([vect.vector(1,0,0)])

        #Just print to say arm was created (for debug)

        print("Arm Created")
        
        
    #Function to print the arm's data to the terminal    
    
    def print_Arm(self):
        
        #Print all link lengths
        
        print("Link lengths (Base to Max Reach):")
        
        for link in self.links:
            
            link.print_Link()
            
        #Print all joint rotation values
            
        print("Joint rotations (Base to furthest Node):")
        
        for joint in self.joints:
            
            joint.print_Joint()
            
        #Print all vectors of one node to the next
            
        print("Vectors (Origin of previous node to next node):")
            
        for vector in self.vectors:
            
            vector.print_vector()
        
        
    
    def add_Joint(self):
     
     if (self.links.size < self.joints.size - 1):
         
         print("Another link is required before adding another degree of freedom")
         
     else:
     
        self.joints = np.append(self.joints, DOF.Joint(0, 0, 0))
        
        print("Joint Added")
        
        
    #Function to add a link to the robot arm, it should not be allowed to add a link if there is not a joint
    #to attach the link to 
        
    def add_Link(self, length):
        
        #Length is the length of the link, if length <= 0 then you cant add the link
        
        if (length <= 0):
            
            print("Cannot attach 0 or negative length link...")
            
        #If there are more links than joints you cannot add a link, need a joint to add a link to
            
        if (self.joints.size < self.links.size + 1):
            
            print("A joint is required before another link is added")
            
        else:
            
        #If everything is cool then add the link to the arm
            
            self.links = np.append(self.links,link.link(length))
            
            self.vectors = np.append(self.vectors, vect.vector(length,0,0))
            
            print("Link Added")
            
    
    #Function to update rotation and position of links based on angles of each joint and length of links
    
    def refresh_Positions(self):
        
        count = 0
        
        for joint in self.joints:
            
            self.vectors[count].rotation_matrix('x',joint.x)
            self.vectors[count].rotation_matrix('y',joint.y)
            self.vectors[count].rotation_matrix('z',joint.z)
            count += 1          
        
        return 
    
    
    
    def plot_Arm(self):
        
        #Create figure object
        
        figure = mpl.figure()
        
        ax = figure.add_subplot(projection='3d')
        
        #Create empty numpy arrays
        
        x = np.array([0])
        y = np.array([0])
        z = np.array([0])
        
        #Iterate through the vectors stored in the arm
        
        for vector in self.vectors:
            
            #Append points into the array
            
            x = np.append(x,vector.x)
            y = np.append(y,vector.y)
            z = np.append(z,vector.z)
        
        
        #plot each of the arrays on the axes
        
        ax.plot(x,y,z, label='Arm', color='g')
        
        #axis labels
        
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.legend()

        # Show the interactive plot window
        mpl.show()
        
        
        return
    
    def rotate_Joint(self, joint, axis, angle):
        
        if (joint >= self.joints.size):
            
            print("Joint does not exist")
            
        else:
            
            self.joints[joint].change_rotation(axis,angle)
        
        return
    
    