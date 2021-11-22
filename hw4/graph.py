from typing import Dict, Set
### You may import any Python's standard library here (Do not import other external libraries) ###


class Graph:
    def __init__(self, edges_path: str, states_path: str) -> None:
        ################## TODO: Fill out the class variables ##################
        #  self._nodes : Set of nodes                                          #
        #  self._neighbors : key: node, value: set of neighbors of node        #
        #  self._node_labels: key: node, value: label of node                  #
        # WARNING: Do not declare another class variables                      #
        ########################################################################
        
        self._nodes: Set[int] = set()
        self._neighbors: Dict[int, Set[int]] = dict()
        self._node_labels: Dict[int, int] = dict()
        
        ######################### Implementation end ###########################

    @property
    def nodes(self) -> Set[int]:
        return self._nodes

    @property
    def neighbors(self) -> Dict[int, Set[int]]:
        return self._neighbors

    @property
    def node_states(self) -> Dict[int, int]:
        return self._node_labels
