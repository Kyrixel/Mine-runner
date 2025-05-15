import titles
import env
import char
import time
import key

if __name__ == "__main__":
    titles.gameTitle()
    print("You need to reach '🎌' to win the game! all the best!!")
    print("\n Starting...")
    time.sleep(1)
    
    char.clear_screen()
    char.mainMenu()
    time.sleep(1)
    char.clear_screen()
    print()
    env.env(char.character, 0, 0)
    
    while not env.killed:
        
        print("1 done")
        pressed = key.keyOutput()
        
        char.clear_screen()
        if pressed == "up":
            env.env(char.character, 0, -1)

        elif pressed == "down":
            env.env(char.character, 0, +1)
            
        elif pressed == "left":
            env.env(char.character, -1, 0)
        
        elif pressed == "right":
            env.env(char.character, +1, 0)
        elif pressed == "quit":
            break
            
        else:
            env.env(char.character, 0, 0)

        
    
    if env.killed == True and env.won == False:
        print("\n You died, try again...")
    elif env.won == True:
        print("\n CONGRATUALTIONS! You won!!")
    else:
        print("\n Restart the game...")
        