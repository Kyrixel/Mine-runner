width = 20
height = 10

char_x = width/2
char_y = height/2

for y in range(height):
    for x in range(width):
        if (x,y) == (char_x, char_y):
            print("🧙", end="")

        
        else:
            print("🟩", end="")
    print() 
