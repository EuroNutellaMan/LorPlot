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

### Python environment
0. Create and enter your python environment if you haven't already (optional except in some linux distributions)
```
python -m venv /path/to/environment
source /path/to/environment/bin/activate # On Linux or MacOS
path\to\environment\Scripts\Activate.bat # On windows cmd.exe, if using powershell use Activate.ps1 instead of Activate.bat
```
1. Install dependencies
```
pip install colorama catppuccin matplotlib numpy
```
2. Clone this repository wherever
```
cd /path/to/installation # For windows use \ instead of /
git clone https://github.com/EuroNutellaMan/LorPlot.git
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
On your preferred terminal run

**Linux and macOS:**
```
python3 /path/to/installation/LorPlot/LorPlot.py
```

**Windows:**
```
python \path\to\installation\LorPlot\LorPlot.py
```

## Notes
This program was only tested on NixOS 23.11 so far.

It is recommended to set up an alias, for terminals using the bash shell this can be done by adding:
```
alias lorplot='python3 path/to/LorPlot/LorPlot.py'
```
to your **~/.bashrc** file

This program is licensed under the **MIT License**
