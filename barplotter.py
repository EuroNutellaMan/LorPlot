#
# LorPlot's bar graph maker
#
from colorama import init, Fore, Style
import matplotlib.pyplot as plt
from catppuccin import PALETTE
import numpy as np
import random
import os

# Initialises colorama
init(autoreset = True)

# Function to convert rgb values in ansi code
def rgbansi(rgb_color):
    return f"\033[38;2;{rgb_color.r};{rgb_color.g};{rgb_color.b}m"

# Defining catppuccin colors
RED = rgbansi(PALETTE.mocha.colors.red.rgb)
GREEN = rgbansi(PALETTE.mocha.colors.green.rgb)
BLUE = rgbansi(PALETTE.mocha.colors.blue.rgb)
PURPLE = rgbansi(PALETTE.mocha.colors.mauve.rgb)
ORANGE = rgbansi(PALETTE.mocha.colors.peach.rgb)
BROWN = rgbansi(PALETTE.mocha.colors.maroon.rgb)
CYAN = rgbansi(PALETTE.mocha.colors.sky.rgb)
PINK = rgbansi(PALETTE.mocha.colors.pink.rgb)
OLIVE = rgbansi(PALETTE.mocha.colors.rosewater.rgb)
GRAY = rgbansi(PALETTE.mocha.colors.mantle.rgb)

# Defining variables
xvalues = [] # Labels for each bar
yvalues = [] # Values for each bar
stddevs = [] # Standard deviation for each bar
graph = []
av_colors = ['tab:blue', 'tab:red', 'tab:orange', 'tab:green', 'tab:purple', 'tab:brown', 'tab:cyan', 'tab:pink', 'tab:olive', 'tab:gray'] # Colors available for the bars
colors = [] # Colors chosen for the bar
prev_choices = []

# Randomly chooses a color sequence
def ColorChooser():
    if len(prev_choices) == len(av_colors) - 1:
        prev_choices.pop(-1)
    a = 1
    while a == 1:
        choice = random.choice(av_colors) # Randomly choses a color
        if choice not in prev_choices: # Makes sure the chosen color is different than the ones chosen before
            a = 0 # Breaks the loop
            return choice
        else:
            a = 1 # Continues the loop

# Define paths
install_path = os.path.abspath(__file__)
install_dir = os.path.dirname(install_path)
csv_file = install_dir + '/plot.csv'

# Reads values from plot.csv and elaborates them
with open(csv_file, 'r') as fl:
    lines = fl.readlines()

for line in lines:
    line = line.split(',') # Splits the line into the values
    line[2] = line[2].strip('\n') # Removes unnecessary \n
    xval = line[0] # Groups labels for each bar
    yval = float(line[1]) # Groups values for each bar
    sdval = float(line[2]) # Groups standard deviations
    xvalues.append(xval)
    yvalues.append(yval)
    stddevs.append(sdval)

# Defines the labels, values, and standard deviation for each bar of the graph
graph = [xvalues, yvalues, stddevs]

# Asks user whether or not to set the colors manually
clrm = input('Do you want to select colors manually? [y/N] ').lower()
if clrm == 'y':
    print(BLUE + '0: Blue')
    print(RED + '1: Red')
    print(ORANGE + '2: Orange')
    print(GREEN + '3: Green')
    print(PURPLE + '4: Purple')
    print(BROWN + '5: Brown')
    print(CYAN + '6: Cyan')
    print(PINK + '7: Pink')
    print(OLIVE + '8: Olive')
    print(GRAY + '9: Gray')
    for i in range(len(xvalues)): # Asks user to set a color for each value
        chosen = int(input(f'Select color for {xvalues[i]}: [0-9] '))
        colors.append(av_colors[chosen])
else:
    for i in range(len(xvalues)): # Randomly applies a color sequence
        chosen = ColorChooser()
        colors.append(chosen)
        prev_choices.insert(0, chosen) # Refresh choices

# Asks user for basic labels
title = input('Title: ')
labelx = input('Label for X axis: ')
labely = input('Label for Y axis: ')

# Asks user if it should build a legend
legquest = input('Include legend? [y/N] ').lower()
incleg = legquest == 'y'

# Builds the bar plot
def bar_plot(graph, labelx, labely, title, colors, incleg):
    xvalues = graph[0] # Label for each bar
    yvalues = graph[1] # Value for each bar
    stddevs = graph[2] # Standard deviation for each bar
    x = xvalues
    y = np.array(yvalues)
    stdv = np.array(stddevs)
    if incleg: # Generates the legend based on colors
        legtit = str(input('Legend title: ')) # Asks user for a legend title
        grp_labels = [] # List of legend labels
        unq_labels = set(colors) # Identifies unique colors
        for label in unq_labels:
            clr = colors[colors.index(label)] # Applies the color to the legend's item
            lbl = str(input(f'Legend label for {clr}: ')) # Asks user for the label represented by the color
            grp_labels.append(plt.Line2D([0], [0], color=clr, lw=4, label=lbl)) # Appends the label and color to the list of legend labels
        plt.legend(handles=grp_labels, title=legtit, loc='best') # Generates the legend in the best position
    plt.bar(x,y, yerr=stdv, linestyle='-', capsize=5.0, color=colors) # Generates the bar plot
    plt.title(title) # Applies title
    plt.ylabel(labely) # Applies label for y axis
    plt.xlabel(labelx) # Applies label for x axis
    plt.grid(axis='y') # Generates gridlines on y axis
    plt.show() # Shows plot in separate window

# Executes funtion to generate the bar plot
bar_plot(graph, labelx, labely, title, colors, incleg)
