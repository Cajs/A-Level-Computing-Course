import random
import time

#sea = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,1,1,1]]
sea = [["~" for _ in range(4)] for _ in range(4)]
locations = [["~" for _ in range(4)] for _ in range(4)]

def placeShips(ships):
    done = False
    count = 0
    while done == False:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if locations[x][y] != "X":
            locations[x][y] = "X"
            count += 1
            if count == ships:
                done = True

def printSea():
    for i in range(0,4):
        for j in range(0,4):
            print(sea[i][j], " ", end='')
        print() #put in a new line
    print()

def guess():
    x,y = "0" , 0
    x = input("What is the X?")
    y = input("What is the Y?")
    fireShot(int(x),int(y))
    if x == "A" or "a":
        x = 0
    elif x == "B" or "b":
        x = 1
    elif x == "C" or "c":
        x = 2
    elif x == "D" or "d":
        x = 3
def checkWin():
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if locations[i][j] == "X":
                count += 1
    if count == 0:
        endGame(True)

def endGame(result):
    if result == True:
        print("YOU WON!")
        quit()
    elif result == False:
        print("GAME OVER")

def fireShot(x,y):
    print("Preparing missile, hang on!")
    time.sleep(1)
    print("Missle loaded!")
    time.sleep(0.5)
    if locations[x][y] == "X":
        print("***WUSHH*** Missile Fired!")
        time.sleep(3)
        print("BOOM, Ship destroyed!")
        sea[x][y] = "X"
        locations[x][y] = "O"
        checkWin()
    elif locations[x][y] == "~":
        print("***WUSHH*** Missile Fired!")
        time.sleep(3)
        print("Splash... No hit there!")
        locations[x][y] = "O"
    elif locations[x][y] == "O":
        print("'scuse me, but you've already hit that location sir, you should hit somewhere else!")
        guess()
    

placeShips(3)
for i in range(0,8):
    guess()
    printSea()
endGame(False)
