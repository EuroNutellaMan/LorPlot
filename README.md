# LorPlot

## Introduction
Simple CLI program to make line and bar plots. Made for a formative activity at UNIFI.

<image src=./Examples/example1.png>

<image src=./Examples/example2.png>

<image src=./Examples/example3.png>

## Installation
### Requirements
- Python 3.11.6 or newer
- Colorama 0.4.6 or newer
- Catppuccin 1.3.2 or newer
- Matplotlib 3.8.0 or newer
- Numpy 1.26.1 or newer
- Linux or MacOS (See usage for Widnows)

### Python environment
0. Create and enter your python environment if you haven't already (optional except in some linux distributions)
```
python -m venv /path/to/environment
source /path/to/environment/bin/activate # On Linux or MacOS
```
1. Clone this repository wherever
```
cd /path/to/installation
git clone https://github.com/EuroNutellaMan/LorPlot.git
cd LorPlot
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. You will find the program in **/path/to/installation/LorPlot**

### NixOS 23.11 or newer
1. Install dependencies via configuration file (or preferred method)
```
environment.systemPackages = with pkgs; [
  (python311.withPackages(ps:  with ps; [
    colorama
    catppuccin
    matplotlib
    numpy
  ]))
];
```
2. Clone this repository in your preferred path
```
cd /path/to/installation
git clone https://github.com/EuroNutellaMan/LorPlot.git
```
3. You will find the program in **/path/to/installation/LorPlot**

## Usage
Write the data in the csv file, with the first column being values for x (line plot) or labels (bar plot), the second column being values for the y axis, and the third column being the standard deviation.
On your preferred terminal run:

**Linux and macOS:**
```
python3 /path/to/installation/LorPlot/LorPlot.py
```

**Windows:**

NOTE: For windows the code needs to be modified with \ instead of / in all paths in all files first. It is recommended to use WSL instead.
```
python C:\\path\to\installation\LorPlot\LorPlot.py
```

### Bar plot
Add data to the plot.csv file in a way where column A contains each bar's label, column B contains its value and column C contains the standard deviation. Each row is a new bar.

<image src=./Examples/BarPlotCsv.png>

<image src=./Examples/BarPlot.gif>

<image src=./Examples/BarPlotResult.png>

### Line plot
Add data to the plot.csv file in a way where column A contains the values of the X axis for every line, column B contains their values for the Y axis, and column C contains the standard deviation. Each time a 0 is encountered in column A a new line starts.

<image src=./Examples/LinePlotCsv.png>

<image src=./Examples/LinePlot.gif>

<image src=./Examples/LinePlotResult.png>

## Notes
This program was only tested on NixOS 23.11 so far.

It is recommended to set up an alias, for terminals using the bash shell this can be done by adding:
```
alias lorplot='python3 path/to/LorPlot/LorPlot.py'
```
to your **~/.bashrc** file

This program is licensed under the **MIT License**
