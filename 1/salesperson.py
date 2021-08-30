#!/user/bin/python3
# File: salesperson.py
# Author: Daniel Lillard
# Date: 08/30/2021
#
# Demo file for the traveling salesperson program.
# Use: python3 salesperson.py n file_name

import sys # for command line arguments

def main():
    """
    The main function.
    """
    # Make sure command line arguments are there.
    if len(sys.argv) < 3:
        print("Fatal Error: Must have 2 command-line arguments.")
        print("Use:\n\tpython3 salesperson.py n file_name")
        exit(1)

    # Get argument values
    file_name = sys.argv[2]
    n = int(sys.argv[1])

    # Open input file
    in_file = open(file_name, "r")
    
    read_and_print(in_file, n)

    in_file.close()
    

def read_and_print(file, num_iterations):
    """
    Reads lines equal to num_iterations from file.
    Prints the resulting coordinates to the command line.
    """
    for i in range(num_iterations):
        line = file.readline()
        x, y = line.split()
        print("Coordinate: ", x, y)

    
if __name__ == "__main__":
    main()


