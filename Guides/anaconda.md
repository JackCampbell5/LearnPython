# How to Learn Anaconda Prompt 

+ Anaconda works in virtual environments called envs that are independent of one another
+ All commands start with "conda" as that is what is being activated
#### Get a command list
+ conda help
#### To create 
1. conda create --name projectName
2. Type "y" and hit enter when prompted 
+ project name can be any words as long as there are no spaces
#### Activate an environment
+ conda activate projectName
+ This activates your project and now all commands should run in it
+ It should now show up as "(projectName) C:\Users\FilePath"
#### Install a dependency:
1. Make sure you have pip installed with "conda install pip"
2. Now install your package with "pip install packageName"
#### List all the packages you have installed
1. conda list