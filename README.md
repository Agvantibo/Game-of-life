![](https://i.ibb.co/ByyNRk9/Untitled.png)

[![Run on Repl.it](https://repl.it/badge/github/Friendly-collab-AgvantiboXGeorgetv4/Game-of-life)](https://repl.it/github/Friendly-collab-AgvantiboXGeorgetv4/Game-of-life)
# Dmitriy's game of life - manual
### Part 1 - Getting ready
For this game to work you should install these packages:
    - gearbox
    - playsound
    - colorama
Gearbox is a custom offline-only package designed to simplify the main code and collect all the tools in one place. If you haven't got it - reclone or update this project...
Playsound and colorama, on the other hand, are autoinstalled on the first run, so no need to worry.
Also you should use a Python 3 interpreter to run this, Python 2 won't do the trick...
### Part 2 - Usage
First, check INPUT. This file is an unextended text file, and could be opened with notepad, nano, vim, or any simple text redactor or IDE. The first four strings set parameters for the game:

**height** - the size of the square field. It is not artificially looped, so gliders and guns can go OOB possybly corrupting them.

**speed** - the time in seconds to wait between the stages of simulation. If set to 0 it will allow manual scrolling with enter.

**dead and live** - symbols for dead and live cells.

###### **IMPORTANT NOTICE**
Due to the way `read()` and `write()` in python work extended ascii table characters entered through file will read incorrectly.
If you want to use these characters, use *console mode*.
Screenshot functionality will be unavailable though...

**Coordinates** - should be entered in the format X Y, and can be natural numbers only.
Save the file after editing it and proceed to launch the game.

The game is started by executing main.py.For Best results use an IDE or Python.exe.
Once started it will produce accurate instructions on what to do.
Happy using!
### Part 3 - Functionality
Besides supporting two input modes and a fancy colorful startup screen this game also contains functions of:
- Screenshots [speed=0, s on execution]
- hackability
- i/o customization
- planned(GUI)