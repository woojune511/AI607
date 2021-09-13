'''
Given the number of nodes N (typically, power of 2), the number of edges E, and four prob. params p_a, p_b, p_c, and p_d,
generate a NxN directed graph.
There can be duplicate edges; keep only one of them.
Add edges until the graph has E edges.

usage: main.py [-h] [-n NUMNODES] [-e NUMEDGES] [-a PA] [-b PB] [-c PC] [-o OUTPUTNAME]

optional arguments:
-n NUMNODES, --numNodes NUMNODES
Select the number of nodes of the graph.
-e NUMEDGES, --numEdges NUMEDGES
Select the number of edges of the graph.
-a PA, --pA PA
The probability of the edge assignment in the partition a.
-b PB, --pB PB
The probability of the edge assignment in the partition b.
-c PC, --pC PC
The probability of the edge assignment in the partition c.
-o OUTPUTNAME, --output OUTPUTNAME
The file name of an output matrix.
'''

import numpy as np
import scipy
import argparse

class hw1(object):
    def __init__(self):
        return


def main():
    n, e, a, b, c, o = [None]*6
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numNodes", help="Select the number of nodes of the graph.")
    parser.add_argument("-e", "--numEdges", help="Select the number of edges of the graph.")
    parser.add_argument("-a", "--pA", help="The probability of the edge assignment in the partition a.")
    parser.add_argument("-b", "--pB", help="The probability of the edge assignment in the partition b.")
    parser.add_argument("-c", "--pC", help="The probability of the edge assignment in the partition c.")
    parser.add_argument("-o", "--output", help="The file name of an output matrix.")
    args = parser.parse_args()
    
    if args.numNodes:
        n = args.numNodes
    if args.numEdges:
        e = args.numEdges
    if args.pA:
        a = args.pA
    if args.pB:
        b = args.pB
    if args.pC:
        c = args.pC
    if args.output:
        o = args.output
    else:
        o = "output"

    return genRMat(n,e,a,b,c,o)


'''
Recursively adds edges in given adjacency matrix.
'''
def genRMat(n,e,a,b,c,o):
    return


if __name__ == "__main__":
    main()


# Where should I declare the adjacency matrix?
# If it is defined in genRMat(), the recursive function will require too much memory.
# It is not desirable.