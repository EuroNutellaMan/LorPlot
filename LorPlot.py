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
csvfile = install_dir + '/plot.csv'

# Check that plot.csv exists
if not os.path.exists(csvfile):
    print(f"plot.csv not found, creating file now!")
    try:
        with open(csvfile, 'w'):
            pass
        print(f"CSV file created successfully at: {csvfile}")
    except Exception as e:
        print(f"Failed to create the CSV file: {e}")
    print(f"Please write values in {csvfile} before using the program!")
    print(f"Make sure to insert 3 values per row!")
    exit

# Print out values in plot.csv
def reviewer():
    missing_value = 0
    print(f"Reading {csvfile}")
    with open(csvfile, "r") as file:
        lines = file.readlines()
    os.system('clear')
    for line in lines:
        check_values = line.split(',')
        if len(check_values) != 3:
            print(f"{RED}{line} INVALID AMOUNT OF VALUES! Must be 3!")
            missing_value = 1
        else:
            try:
                float(check_values[2])
                float(check_values[1])
                print(f"{GREEN}{line}")
            except:
                print(f"{RED}{line} INVALID VALUES! 2nd and 3rd column must be numbers!")
                missing_value = 1
    if bool(missing_value):
        print(f"{RED}One or more rows are invalid, please edit the csv file to fix this!")
    else:
        print(f"{GREEN}Everything seems in order!")
        proceed = input("Press enter to go back to selection: ")
        selector()

# Function to choose type of graph
def selector():
    os.system('clear') # Clears the terminal
    print(YELLOW + 'Select graph style')
    print(GREEN + '1: Line plot')
    print(BLUE + '2: Bar plot')
    print(YELLOW + '9: Review plot.csv')
    print(RED + '0: Exit')
    choice = input('Select option [1-2, 0]: ')
    if choice == '0': # Exits the program
        print(RED + 'Exiting.')
    elif choice == '1': # Starts the line plotter
        subprocess.Popen(['python3', lineplotter]).wait()
    elif choice == '2': # Starts the bar plotter
        subprocess.Popen(['python3', barplotter]).wait()
    elif choice == '9':
        reviewer()
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
