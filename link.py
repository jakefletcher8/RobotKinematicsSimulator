# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:27:38 2026

@author: jakef
"""

#Links to connect degrees of freedom for the robot

class link():
    def __init__(self, length):
        
        self.length = length
        
        print("Link created")
        
        
    def print_Link(self):
        
        print(self.length)
        
    def change_length(self,length):
        
        self.length = length