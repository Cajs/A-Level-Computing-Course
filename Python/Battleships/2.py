import random
#0 = sea
#0 = ship
#2 = hit ship
#sea = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
sea = [["~" for _ in range(4) ] for _ in range(4) ]
location = [["~" for _ in range(4) ] for _ in range(4) ]

ships = input()
def grid():
        for x in range(0,4):
                for y in range(0,4):
                        print(sea[x][y] , " " , end='')
                print()
        print()
def placeships(ships):
        done = False
        count = 0
        while done == False:
                x = random.ranint(0,3)
                y = random.ranint(0,3)
                if locations[x][y] !="X":
                        locations[x][y] = "X"
                        count += 1
                        if count == ships:
                                done = True

def guess():
        x,y = 0
        print("What is your X value?")
        x = input()
        print("What is your Y value?")
        y = input()
        fireshot(int(x),ing(y))

def checkwin():
        count = 0
        for i in range(0,4):
                for j in range(0,4):
                        if location[i][j] == "X":
                                count += 1
        if count == 0:
                endgame(True)

def endgame(result):
        if result == True:
                print("You are a winner")
                quit()
        elif result == False:
                print ("You lost")

def fireshot(x,y):
        print("Missile fired!")
        print("***Missile noises***")
        if location[x][y] == "X":
                print("BOOM, Ship desroyed!")
                sea[x][y] = "X"
                loaction[x][y] = "O"
                checkwin()
        elif location[x][y] == "~":
                print("Splash... No hit there!")
                location[x][y] == "O"
        elif location[x][y] == "O":
                print("'scuse me, but you've already hit that location sir!")
                guess()
placeships(3)
for i in range(0,8):
        guess()
        printsea()
endgame(False)
