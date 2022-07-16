# Boomboom by Sean Layton and Lourenzo Kodama

Terminal-based game with an epic BYU vs Utah twist called BOOMBOOM!

### Prerequisites

* Install the package termcolor - "sudo pip3 install termcolor"

### Running

* Start the game using "python3.5 run.py"
* Terminal should be maximized for best experience.

### Controls

* W - Move Up
* A - Move Left
* S - Move Down
* D - Move Right
* B - Drop a boomboom

### Objective

* You cannot destroy solid walls with boom
* You can destroy brick walls with boom
* The aim is to kill all the enemies
* You die if you bump into an enemy or if you get boomed

### Install/Syntax for Climage (Display images in Terminal) (Didn't work haha) 

Taken from the Climage website 
- Sean Layton

pip install climage

convert(filename, is_unicode=False, is_truecolor=False, is_256color=True, is_16color=False, is_8color=False, width=80, palette=”default”)

Parameters:
filename : Name of image file.
is_unicode :  If true, conversion is done in unicode format, otherwise ASCII characters will be used.
is_truecolor :  Whether to use RGB colors in generation, if supported by terminal. Defaults False.
is_256color : Whether to use 256 colors encoding. Defaults True.
is_16color : Whether to use 16 colors encoding. Defaults False.
is_8color : Whether to use first 8 System colors. Defaults False.
width : Number of blocks of console to be used. Defaults to 80.
palette : Sets mapping of RGB colors scheme to system colors. Options are : [“default”, “xterm”, “linuxconsole”, “solarized”, “rxvt”, “tango”, “gruvbox”, “gruvboxdark”]. Default is “default”.

to_file(infile, outfile, is_unicode=False, is_truecolor=False, is_256color=True, is_16color=False, is_8color=False, width=80, palette=”default”)

Parameters:
infile : The name/path of image file.
outfile :   File in which to store ANSI encoded string.

Example: 

import climage

# converts the image to print in terminal
# inform of ANSI Escape codes
output = climage.convert('boom.png')

# prints output on console.
print(output)

Example 2 (Save encoding to file) 

import climage

# saves the converted encoded string
# to banana_ansi file.
output = climage.to_file('boom.png', 'boom_ansi')



