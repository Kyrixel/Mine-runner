import key
import random


damage = "💥"
goal = "🎌"
width = 20
height = 10

char_x = width/2
char_y = 0

won = False
killed = False

mines = []

winner = (((random.randint(0, width), random.randint(0, height))))


for _ in range(5):
    x = random.randint(0, width)
    y = random.randint(0, height)
    mines.append((x,y))

moved = []
print((winner))
def env(character, xc, yc):
    global mines, char_x, char_y, killed, won, moved
    
    char_x += xc
    char_y += yc

    moved.append((char_x, char_y))
    if char_y >= height:
        char_y -= yc
    elif char_y < 0:
        char_y -= yc
    elif char_x >= width:
        char_x -= xc
    elif char_x < 0:
        char_x -= xc
    print(winner)


    for y in range(height):
        for x in range(width):

            if (x,y) == (char_x, char_y):
                print(character, end="")
            elif (x,y) in moved:
                print("🟨", end="")


            elif (x,y) == winner:
                print(goal, end="")

            elif (char_x, char_y) in mines:
                print(damage, end="")
                killed = True
                won = False

            elif (char_x, char_y) == winner:
                print(goal, end="")
                killed = True
                won = True
            else:
                print("🟩", end="")
            
            
        print()


