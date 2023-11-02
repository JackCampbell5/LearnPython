# Set Up To Code and use Python 

## Anaconda
In python to deal with dependency's(Library's of code used to make coding easier) you need something called a python 
interpreter. My favorite one is called Anaconda, so you can code multiple different projects on the same machine.
#### To install:
1. Download from https://www.anaconda.com/download
2. Go through the installation process and use all the default settings
#### To create a project(Command hints in [Anaconda Hints](anaconda.md)):
1. Create a environment with: conda create --name projectName
2. Active the environment with: conda activate projectName
3. Install the package manager pip(You dont need to know what that means): conda install pip

## Pycharm
I always recommend using jetbrains projects for programming because I like there autocomplete, and they are usually 
better for new programmers and is just more fun to use. 
#### To install:
1. Download Jetbrains toolbox https://www.jetbrains.com/lp/toolbox/ using all the default options
2. Locate and download Pycharm
#### Set up this project:
1. Click "Get from VCS" at the top 
2. Click "Repository URL" on the left sidebar
3. Under "Url" copy: https://github.com/JackCampbell5/LearnPython.git 
4. Click "Clone"
5. If asked for a python interpreter click conda and find yours if it exists or create a new one
6. In the top right corner the thing with the arrow next to it should say "Current File", click and change it to if it does not