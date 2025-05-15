# Mine-runner
python game without any external modules, only used os, time, termios, tty and random. all of them are included in the standard library. 
termios and tty are Unix-specific

-----
## Aim 
Need to reach '🎌' to win the game, there are 5 mines hidden around the region if you step on them you lose.

-----
### Files

- char.py - contains the character selection screen
- env.py - creates the env and manages position of the user on the screen matrix
- key.py - all the keybindings using sys, termios and tty
- titles.py - contains the ascii titles
- main.py - combines all of them and displays it all in a series 
