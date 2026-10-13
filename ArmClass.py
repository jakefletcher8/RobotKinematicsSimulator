# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:22:01 2026

@author: jakef

Arm class to have a defined length and structure to an arm
"""

import DOFClass as DOF
import numpy as np
import link

class ArmPart():
    def __init__(self):
        
        self.links = np.array([link.link(1)])
        self.joints = np.array([DOF.Joint(0, 0, 0)])

        print("Arm Created")
        
        
    def print_Arm(self):
        
        print("Link lengths (Base to Max Reach):")
        
        for link in self.links:
            
            link.print_Link()
            
        print("Joint rotations (Base to furthest Node):")
        
        for joint in self.joints:
            
            joint.print_Joint()
        
        
    
    def add_Joint(self):
     
     if (self.links.size < self.joints.size):
         
         print("Another link is required before adding another degree of freedom")
         
     else:
     
        self.joints = np.append(self.joints, DOF.Joint(0, 0, 0))
        print("Degree of freedom Added")
        
    def add_Link(self, length):
        
        if (length <= 0):
            
            print("Cannot attach 0 or negative length link...")
            
        if (self.joints.size < self.links.size):
            
            print("A joint is required before another link is added")
            
        else:
            
            self.links = np.append(self.links,link.link(length))
            print("Link Added")
        
        
        
        