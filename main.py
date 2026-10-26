import ArmClass as ArmC
import matplotlib.pyplot as mpl

import tkinter as tk

'''

TO DO: 
    
    -Write main loop to allow user to easily make computations
    -Make some sort of UI
    -Animate moving vectors to show how the rotation happens in real time
    -Allow user to change how many degrees of freedom the simulation contains
    -Allow user to change the length of given 'arms'
    -Make it so that arms cannot phase through each other or display an error when this occurs


'''

Arm = ArmC.ArmPart()

Arm.plot_Arm()

Arm.do_rotation(0, 'y', 60)

Arm.print_Arm()




Arm.plot_Arm()












