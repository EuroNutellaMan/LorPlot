#
# LorPlot's line graph maker
#
import matplotlib.pyplot as plt
import numpy as np

# Defining variables
xvalues = [] # Labels for each bar
yvalues = [] # Values for each bar
stddevs = [] # Standard deviation for each bar
graphs = []
graph = []
xgr = []
ygr = []
sdgr = []

# Define paths
install_path = os.path.abspath(__file__)
install_dir = os.path.dirname(install_path)
csv_file = install_dir + 'plot.csv'

# Reads values from plot.csv and elaborates them
with open(csv_file, 'r') as fl:
    lines = fl.readlines()

for line in lines:
    line = line.split(',') # Splits the line into the values
    line[2] = line[2].strip('\n') # Removes unnecessary \n
    xval = float(line[0]) # Groups values for the x axis
    yval = float(line[1]) # Groups values for the y axis
    sdval = float(line[2]) # Groups standard deviations
    xvalues.append(xval)
    yvalues.append(yval)
    stddevs.append(sdval)

# Asks user for basic labels
title = input('Title: ')
labelx = input('Label for X axis: ')
labely = input('Label for Y axis: ')

# Builds a new line every time it encounters a value of 0 for the x axis
for i in range(len(xvalues)):
    if xvalues[i] == 0 and i != 0: # Starts new line
        graph = [xgr, ygr, sdgr] # Defines the line with the grouped values
        graphs.append(graph) # Appends previous line to the graph
        graph = [] # Reset line
        xgr = [xvalues[i]] # Groups values for x axis
        ygr = [yvalues[i]] # Groups values for y axis
        sdgr = [stddevs[i]] # Groups standard deviations
    xgr.append(xvalues[i])
    ygr.append(yvalues[i])
    sdgr.append(stddevs[i])
graph = [xgr, ygr, sdgr]
graphs.append(graph) # Appends the last line

# Function that generates the line graph
def line_plot(graphs, labelx, labely, title):
    leglables = []
    for graph in graphs:
        leglable = input('Graph name: ') # Asks user to name every line
        leglables.append(leglable)
        xvalues = graph[0]
        yvalues = graph[1]
        stddevs = graph[2]
        x = np.array(xvalues)
        y = np.array(yvalues)
        stdv = np.array(stddevs)
        plt.errorbar(x,y, yerr=stdv, capsize=5, linestyle='-', marker='^') # Generates the lines
    plt.title(title) # Applies title to graph
    plt.ylabel(labely) # Applies label to y axis
    plt.xlabel(labelx) # Applies label to x axis
    plt.legend(leglables, loc='best') # Displays legend
    plt.grid() # Shows grid on x and y axis
    plt.show() # Shows the line graph in a separate window

# Executes function to build the graph
line_plot(graphs, labelx, labely, title)
