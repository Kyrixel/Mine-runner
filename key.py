import sys
import termios
import tty

Condition = True

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == '\x1b':
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            return ch1 + ch2 + ch3
        else:
            return ch1
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)



def keyOutput():
    global Condition
    
    key = get_key()
        
    if key == '\x1b[A':
        return "up"
    
    elif key == '\x1b[B':
        
        return "down"
    
    elif key == '\x1b[C':
        return "right"
    
    elif key == '\x1b[D':
        return "left"
    
    elif key == '\r':
        return "enter"
    
    elif key == 'q':
        return "quit"
        



if __name__ == "__main__":
    while Condition:
        keyOutput()