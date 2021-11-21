import argparse
import numpy as np
import random
from SIR import sampleInitialNodes, runSimulation
# import time

# start = time.time()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("input", metavar="INPUT", type=str, default='graph.txt', help="a path containing input graph")
    parser.add_argument("--beta", metavar="BETA", type=float, default=0.0, help="the infection rate of the SIR model")
    parser.add_argument("--delta", metavar="DELTA", type=float, default=1.0, help="the recovery rate of the SIR model")
    parser.add_argument("--initial-nodes", metavar="INITIAL_NODES", type=int, default=0, help="a target number of initial nodes")
    parser.add_argument("--seed", metavar="SEED", type=int, default=0, help="a random seed")
    args=parser.parse_args()

    try:
        node_to_idx={}
        edges=set([])
        with open(args.input, "r") as f:
            for line in f:
                u, v = line.strip().split()
                if u == v: continue
                if u not in node_to_idx:
                    node_to_idx[u] = len(node_to_idx)
                if v not in node_to_idx:
                    node_to_idx[v] = len(node_to_idx)
                edges.add((node_to_idx[u], node_to_idx[v]))
                edges.add((node_to_idx[v], node_to_idx[u]))
            num_nodes = len(node_to_idx)
            edges = list(edges)
    except:
        print('ERROR: FILE DOES NOT EXIST!')
        exit(0)

    random.seed(args.seed)
    np.random.seed(args.seed)

    total_sum = 0
    for i in range(100):
        initial_nodes = sampleInitialNodes(num_nodes, args.initial_nodes)
        total_sum += runSimulation(num_nodes, edges, initial_nodes, args.beta, args.delta)

    print('average influenced nodes:', total_sum / 100.0)
    # print('total time taken:', time.time()-start)