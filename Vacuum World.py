import random
import sys

class environment:
    print ("\nWelcom to Vacuum World!")
    def __init__(self):
        self.array = [[random.choice(['dirty', 'clean']) for col in range(2)] for row in range(1)]
    def displayGrid(self):
        print("\n+-------+-------+")
        for i in self.array:
            print("|", end=" ")
            for j in i:
                print(j, end=" | ")
            print("\n+-------+-------+")
            
class vacuumCleaner:
    def __init__(self,env):
        self.env=env
        self.position =(0,0)
        print ("Vacuum starts at (0,0)")

    def vacuumCleaning(self):
        row, col = self.position
        if self.env.array [row][col] == 'dirty':
            self.env.array[row][col] = 'clean'
            self.env.displayGrid() 
            print (f"({row},{col}) has been cleaned")
        else: 
            self.env.displayGrid() 
            print (f"({row},{col}) does not need to clean, vacuum move.")

class vacuumMovement:
    def __init__(self, vac):
        self.vac = vac

    def randomMove(self):
        row,col=self.vac.position 
        direction = random.choice([-1,1]) 
        movement = col + direction
        if movement < 0:
            movement = 0
            print ("There is wall, Vacuum can not move to left!")
        elif movement > 1:
            movement = 1
            print ("There is wall, Vacuum can not move to right!")
        else: 
            print (f"Vacuum move to ({row},{movement})")

        self.vac.position =(row,movement)
        self.vac.vacuumCleaning() 

    def headingHome(self):
        if self.vac.env.array [0][0]=='clean' and self.vac.env.array [0][1]=='clean':
            self.randomMove()
            self.vac.env.displayGrid() 
            print ("All clean! Heading home")
            sys.exit("Bye Bye!")
        else:
            self.randomMove()
            self.headingHome()
env=environment()
env.displayGrid()
vac=vacuumCleaner(env)
mov=vacuumMovement(vac)
mov.headingHome()



