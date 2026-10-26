import ArmClass as ArmC


import tkinter as tk

'''

TO DO: 
    
    -Write main loop to allow user to easily make computations
    -Make some sort of UI
    -Animate moving vectors to show how the rotation happens in real time
    -Allow user to change the length of given 'arms'
    -Make it so that arms cannot phase through each other or display an error when this occurs


'''

Arm = ArmC.ArmPart()

Arm.add_Joint()

Arm.add_Link(5)

Arm.add_Joint()

Arm.add_Link(3)

Arm.plot_Arm()

Arm.do_rotation(0, 'y', 60)

Arm.do_rotation(2, 'y', 30)

Arm.print_Arm()

Arm.plot_Arm()












