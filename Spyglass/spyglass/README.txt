The idea of this task is to collect data from regression results. Run the script. It will generate regression results.
Your task is to collect the results of it. For this example lets consider it as a Spyglass regression.
(Spyglass is one of many Synopsys tools, if interested ask for more details)

The results of the regression is located in folder <config_name>/spyglass/spyglass.html
You need to take that html file and connect it into one file. Not only that, we need to understand what folder does it belong to, so you will need to modify the html file to include the folder name from which it is taken.

Your script should work like this
>script.py lib <additional argument as output file name>

Notes
Additional argument can be given as an output file, otherwise give a default one.
Caution!
HTML file might be missing in some directories, make sure to print those directories!

Hints n Tips
Remember functions to work with files
<file_handle> = open('file_name','mode')
<file_handle>.read()  <- read the whole file as one big string
<file_handle>.readlines()  <- reads the file line by line and returns array.
<file_handle>.write("string") <- write to file
<file_handle>.close()  <- once done with file, close it!

Command line arguments can be taken using sys built in module
import sys
sys.argv  <- this will return all command line options as a list

You might also need os module. Here are some os module functions you may need
os.getcwd() <- returns current path.
os.system() <- does commands of operating system, example os.system('ls -all')
os.path.exists  <- returns True if the file mentioned as an argument exists, False otherwise


Step 2. Give arguments using argparse module

In some cases you need to give certain arguments and you need the script to work no matter the order of arguments 
givven. That can be done using argparse module

Script usage without Argparse
script.py lib file_name  <- works
script.py file_name lib <- error!

Script usage with Argparse
script.py -p lib -o file_name <-works
script.py -o file_name -p lib <- also works!

Basic building blocks.Import the module itself.

import argparse

Create an argument parser, you may have different ones.

parser = argparse.ArgumentParser(description='Script description goes here')

Add arguments that you need

parser.add_argument('-p', '--path',type=str,help='Path to regression folder', required=True)

parse your arguments with your parser

parser.parse_args(['You may give command line options here'])

For the task you will need 2 arguments, 1 input directory name and 2nd output file.
Directory name is REQUIRED. Output file is not.

SCRIPT REQUIREMTNS:
It should take directory name as input and collect data from that path
Script should print Directories that did not have the html file.
You need to handle wrong arguments properly. No crushing, print error/help and exit. 
In both versions of the script should have some sort of help. 
Make sure your script is "callable" from any directory. 
