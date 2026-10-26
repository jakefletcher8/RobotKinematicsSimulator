import ArmClass as ArmC
import matplotlib.pyplot as mpl

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

Arm.rotate_Joint(0, 'y', 90)



Arm.print_Arm()

Arm.refresh_Positions()

Arm.refresh_Positions()

Arm.refresh_Positions()

Arm.rotate_Joint(0, 'y', -90)
Arm.rotate_Joint(0, 'z', 90)



Arm.refresh_Positions()



Arm.plot_Arm()

Arm.print_Arm()










