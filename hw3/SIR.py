import numpy as np
import random
### TODO: only importing INTERNAL libraries are allowed except for NumPy ###
import collections
############################################################################


def sampleInitialNodes(num_nodes, num_initial_nodes):
    """ 
    Implement the function that samples the initial active nodes.
    
    Inputs:
        num_nodes: the number of nodes N in the given graph. 
        num_initial_nodes: the target number of initial active nodes N_0.
        
    Output: a list of N_0 initial active nodes
    """
    ### TODO: WRITE YOUR CODE HERE ###
    return random.sample(range(num_nodes), num_initial_nodes)
    ##################################

def runSimulation(num_nodes, edges, initial_nodes, beta, delta):
    """ 
    Implement the function that counts the ultimate number of recovered nodes.
    
    Inputs:
        num_nodes: the number of nodes in the input graph. 
        edges: a list of tuples of the form (u, v),
          which indicates that there is an edge from u to v. 
          You can assume that there is no isolated node.
        initial_nodes: a list of initial active nodes.
        beta: the infection rate of the SIR model
        delta: the recovery rate of the SIR model
        
    Output: the number of recovered nodes after the diffusion process ends.
    """
    ### TODO: WRITE YOUR CODE HERE ###
    # 0: susceptible, 1: infected, 2: recovered
    node_states = [0] * num_nodes
    for node in initial_nodes:
        node_states[node] = 1
    node_states = np.array(node_states, dtype=np.int8)

    print(len(edges))
    
    while np.any(node_states == 1):
        # node_to_infect = []
        # node_to_recover = []
        # node_update = set()
        node_update = np.zeros(num_nodes, dtype=np.int8)
        # susceptible_nodes = np.where(node_states == 0)[0]
        infected_nodes = np.where(node_states == 1)[0]

        # prob = np.random.rand(num_nodes)


        # print(infected_nodes)
        for (u, v) in edges:
            # print(f'u {u}, infected_node: {infected_node}, node_states[v] {node_states[v]}')

            if node_states[u] != 1 or node_states[v] != 0:
                continue

            if np.random.rand() < beta:
                # node_update.add(v)
                node_update[v] += 1

        for u in infected_nodes:
            if np.random.rand() < delta:
                # node_update.add(u)
                node_update[u] += 1

        # for node in node_update:
            # node_states[node] += 1
        node_update = np.where(node_update > 0, 1, 0)
        node_states = node_states + node_update
        
        # print(f'node_updates: {collections.Counter(node_update)}')

        # break

        # print(f'{collections.Counter(node_states)}')
    # print('one iteration is over')

    return np.count_nonzero(node_states == 2)
    ##################################
