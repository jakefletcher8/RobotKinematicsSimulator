# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:27:38 2026

@author: jakef
"""

#Links to connect degrees of freedom for the robot

#Link object to store the length of each link

class link():
    def __init__(self, length):
        
        #Length of link stored as a value
        
        self.length = length
        
        #Print statement for debug
        
        print("Link created")
        
        
    #Print the value of the length
        
    def print_Link(self):
        
        print(self.length)
        
    #Change the length of the link
        
    def change_length(self,length):
        
        self.length = length