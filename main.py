import ArmClass as ArmC

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

Arm.add_Joint()

Arm.add_Joint()

Arm.add_Link(7)

Arm.add_Link(1)

Arm.add_Link(2)

Arm.print_Arm()





