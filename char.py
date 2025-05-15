import key
import os
import time
import titles


charSelection = True


char_list = ["🧙","👾","👤","👨","👮","🤴","👼","🕺","🦼","🐶","🐱","🐭","🐹","🐰","🦊","🐨","🐯","🦁","🐮","🐷","🐸","🐧","🐣","🦋","🐳","🦖","🦚","🍁","🤸"]

character = char_list[0] # default kara hai ye

index = 0

def clear_screen():
    os.system('clear')


def menu():
    
    global index
    global character 
    global charSelection
    global char_list

    

    for i in range(len(char_list)):
        if i == index:
            print(" ➡️ ", char_list[i], "⬅️ ", end= " - " )
        else:
            print(char_list[i], end= " - ")
    


def inputs():
    global index
    global character 
    global charSelection
    global char_list

    print()
    pressed = key.keyOutput()
    

    if pressed == "left":
        
        index -= 1

    elif pressed == "right":
        
        index += 1

    elif pressed == "enter":
        
        character = char_list[index]
        charSelection = False
    
    elif pressed == "quit":
        charSelection = False







def mainMenu():

    
    global charSelection 
    charSelection = True

    while charSelection:
        titles.charTitle()
        print("\n Select your character using arrow keys, press 'Enter' to lock in (Press 'q' to exit) \n")
        menu()
        inputs()
        time.sleep(0.1)
        clear_screen()
    
    print("your character is -> ", character)
    print("Loading game...")
        

if __name__ == "__main__":
    mainMenu()
        


