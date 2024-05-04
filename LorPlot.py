#
# LorPlot
# by Lorenzo Brzek
#
from colorama import init, Fore, Style
from catppuccin import PALETTE
import subprocess
import time
import os

# Initializes colorama
init(autoreset = True)

# Function to convert rgb values in ansi code
def rgbansi(rgb_color):
    return f"\033[38;2;{rgb_color.r};{rgb_color.g};{rgb_color.b}m"

# Defines catppuccin colors
YELLOW = rgbansi(PALETTE.mocha.colors.yellow.rgb)
RED = rgbansi(PALETTE.mocha.colors.red.rgb)
GREEN = rgbansi(PALETTE.mocha.colors.green.rgb)
BLUE = rgbansi(PALETTE.mocha.colors.blue.rgb)

# Define paths
install_path = os.path.abspath(__file__)
install_dir = os.path.dirname(install_path)
lineplotter = install_dir + '/lineplotter.py'
barplotter = install_dir + '/barplotter.py'

# Function to choose type of graph
def selector():
    os.system('clear') # Clears the terminal
    print(YELLOW + 'Select graph style')
    print(GREEN + '1: Line plot')
    print(BLUE + '2: Bar plot')
    print(RED + '0: Exit')
    choice = input('Select option [1-2, 0]: ')
    if choice == '0': # Exits the program
        print(RED + 'Exiting.')
    elif choice == '1': # Starts the line plotter
        subprocess.Popen(['python3', lineplotter]).wait()
    elif choice == '2': # Starts the bar plotter
        subprocess.Popen(['python3', barplotter]).wait()
    else: # Restarts in case of bad prompt from user
        print(RED + 'Invalid input! Try again!')
        print(RED + 'Restarting in 3...')
        time.sleep(1)
        print(RED + '2...')
        time.sleep(1)
        print(RED + '1...')
        time.sleep(1)
        selector()

# Executes funciton to select graph type
selector()
