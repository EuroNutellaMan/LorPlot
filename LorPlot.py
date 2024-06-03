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

# Opens the default editor for that file
def edit_file(file):
    os.system(f"$EDITOR {file}")

# Print out values in plot.csv
def reviewer():
    print("Reviewing the plot csv file")
    missing_stdev = 0
    invalid_values = 0
    print(f"Reading {csvfile}")
    with open(csvfile, "r") as file:
        lines = file.readlines()
    os.system('clear')
    print(f"{GREEN}plot.csv review:")
    print(f"{GREEN}label/x, y, std-dev")
    print(f"{GREEN}-------------------")
    updated_lines = []
    for line in lines:
        line = line.strip("\n")
        check_values = line.split(',')
        if len(check_values) != 3:
            line = line + ",0"
            print(f"{YELLOW}{line} MISSING ST. DEV! Assigning 0 to it.")
            missing_stdev = 1
        else:
            try:
                float(check_values[2])
                float(check_values[1])
                print(f"{GREEN}{line}")
            except:
                print(f"{RED}{line} INVALID VALUES! 2nd and 3rd column must be numbers!")
                invalid_values = 1
        updated_lines.append(line)
    if bool(missing_stdev):
        with open(csvfile, "w") as file:
            for line in updated_lines:
                file.write(f"{line}\n")
        print(f"{GREEN}-------------------")
        proceed = input("Press enter to continue! ")
    elif bool(invalid_values):
        print(f"{GREEN}-------------------")
        print(f"{RED}One or more rows are invalid, please edit the csv file to fix this!")
        answer = input(f"{YELLOW}Edit the csv file? [y to edit; anything else will quit]: ").lower()
        if answer == "y":
            edit_file(csvfile)
    else:
        print(f"{GREEN}-------------------")
        print(f"{GREEN}Everything seems in order!")
        proceed = input("Press enter to continue! ")

# Function to choose type of graph
def selector():
    os.system('clear') # Clears the terminal
    print(YELLOW + 'Select graph style')
    print(GREEN + '1: Line plot')
    print(BLUE + '2: Bar plot')
    print(YELLOW + '8: Edit plot.csv')
    print(YELLOW + '9: Review plot.csv again')
    print(RED + '0: Exit')
    choice = input('Select option [1-2, 0]: ')
    if choice == '0': # Exits the program
        print(RED + 'Exiting.')
    elif choice == '1': # Starts the line plotter
        subprocess.Popen(['python3', lineplotter]).wait()
    elif choice == '2': # Starts the bar plotter
        subprocess.Popen(['python3', barplotter]).wait()
    elif choice == '8':
        edit_file(csvfile)
        selector()
    elif choice == '9':
        reviewer()
        selector()
    else: # Restarts in case of bad prompt from user
        print(RED + 'Invalid input! Try again!')
        print(RED + 'Restarting in 3...')
        time.sleep(1)
        print(RED + '2...')
        time.sleep(1)
        print(RED + '1...')
        time.sleep(1)
        selector()

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
    answer = input(f"{YELLOW}Edit the csv file? [y to edit; anything else will quit]: ").lower()
    if answer == "y":
        edit_file(csvfile)
    else:
        print(f'{RED}Exiting!')
        exit

# Executes funcitons to review and select graph type
reviewer()
selector()
