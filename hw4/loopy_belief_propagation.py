from typing import Dict


def loopy_belief_propagation(
    graph: Graph,
    max_iters: int,
    tol: float,
) -> Dict[int, Dict[int, float]]:
    belief: Dict[int, Dict[int, float]] = dict()
    ####### TODO: Implement the loopy belief propagation algorithm #########
    #  belief : key: node, value: dictionary in which the key is state and # 
    #  the value is belief of state                                        #
    ########################################################################
    for itr in range(maxiters):

        #### Check the convergence ###
        # Stop the iteration if L1norm[belief(t) - belief(t-1)] < tol
        delta: float = 0.0
        print(f"[Iter {itr}]\tDelta = {delta}")

        if delta < tol:
            break
    ######################### Implementation end #########################

    return belief