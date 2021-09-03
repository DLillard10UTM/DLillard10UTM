#!/user/bin/python3
# File: salesperson.py
# Author: Daniel Lillard
# Date: 08/30/2021
#
# Demo file for the traveling salesperson program.
# Use: python3 salesperson.py n file_name

import sys # for command line arguments
import itertools # we use this to create the permutations.
from math import sqrt #For getting the distance.

def main():
    #The main function.
    # Make sure command line arguments are there.
    if len(sys.argv) < 3:
        print("Fatal Error: Must have 2 command-line arguments.")
        print("Use:\n\tpython3 salesperson.py n file_name")
        exit(1)

    # Get argument values
    file_name = sys.argv[2]
    n = int(sys.argv[1])

    # Open input file, read it in, and close it.
    in_file = open(file_name, "r")
    ourPoints = read_and_save(in_file, n)
    in_file.close()

    createPerms(ourPoints)
    

def read_and_save(file, num_iterations):
    #Reads lines equal to num_iterations from file.
    #Prints the resulting coordinates to the command line.
    ourPoints = []
    for i in range(num_iterations):
        line = file.readline()
        x, y = line.split()
        x = int(x)
        y = int(y)
        ourPoints.append((x,y))
    return ourPoints
            

#let's go ahead and create all perms.
def createPerms(ourPoints):
    ourPerms = list(itertools.permutations(ourPoints))
    lowestDist = 0
    dist = 0
    #here we get each perm, get the distance travels, and compare it to the lowest.
    for permIndex in range(len(ourPerms)):
        for i in range(len(ourPoints) - 1):
            dist += sqrt((ourPerms[permIndex][i][0]-ourPerms[permIndex][i+1][0])**2 + 
                        (ourPerms[permIndex][i][1]-ourPerms[permIndex][i+1][1])**2)
        dist += sqrt((ourPerms[permIndex][0][0]-ourPerms[permIndex][-1][0])**2 + 
                (ourPerms[permIndex][0][1]-ourPerms[permIndex][-1][1])**2)
        if(permIndex == 0):
            lowestDist = dist
            lowestPerm = ourPerms[permIndex]
        else:
            if(dist < lowestDist):
                lowestDist = dist
                lowestPerm = ourPerms[permIndex]
        dist = 0
    print(lowestDist)
    print(lowestPerm)

if __name__ == "__main__":
    main()