import os
import subprocess
import sys

###############
# Constants #
###############
# Path to the executable
executable_path = os.path.join(os.path.dirname(__file__), 'executable')
# Path to the input file
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
#start engine
engine = subprocess.Popen([executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
