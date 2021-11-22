import os
from typing import Dict
from graph import Graph
from loopy_belief_propagation import loopy_belief_propagation


if __name__ == "__main__":
    ############################################################################
    # Each line of the edges file(polblogs_edges.txt, pubmed_edges.txt)        #
    # looks like:                                                              #
    #         <SOURCE NODE ID> <DESTINATION NODE ID>                           #
    # s.t. two integers are separated by space                                 #
    # ------------------------------------------------------------------------ #
    # Each line of the labels file(polblogs_labels.txt, pubmed_labels.txt)     #
    # looks like:                                                              #
    #         <NODE ID> <LABEL ID>   or   <NODE ID>                            #
    # s.t. <NODE ID> <LABEL ID> are separated by space                         #
    ############################################################################
    
    edges_path = os.path.join(os.pardir, "graphs", "polblogs_edges.txt")
    labels_path = os.path.join(os.pardir, "graphs", "polblogs_labels.txt")
    # edges_path = os.path.join(os.pardir, "graphs", "pubmed_edges.txt")
    # labels_path = os.path.join(os.pardir, "graphs", "pubmed_labels.txt")
    maxiters = 200
    tolerance = 1e-4

    # Initialize the graph
    graph: Graph
    graph = Graph(edges_path, labels_path)

    # Run the loopy belief propagation algorithm
    belief: Dict[int, Dict[int, float]]
    belief = loopy_belief_propagation()

    # Save the result file
    ################ TODO: Save the result of the algorithm ################
    #  result file name should  XXX_belief.txt                             #
    #  (XXX: name of graph, e.g., polblogs, pubmed)                        #
    #                                                                      #
    #  Each line of the result file looks like:                            #
    #   <NODE ID> <STATE ID>:<STATE BELIEF> <STATE ID>:<STATE BELIEF> ...  #
    # s.t. STATE ID and STATE BELIEF are separated by ":", and NODE ID and #
    # each <STATE ID>:<STATE BELIEF> pairs are separated by space          #
    ########################################################################
        
    
        
    ######################### Implementation end ###########################

