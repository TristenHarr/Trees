"""
NP-Tree

The NP-Tree is a data-structure built completely on top of the concept of OOP in combination with functional
programming. The primary goal of the NP-Tree is to create a data-structure that is large enough that it can be
considered a framework in and of itself, built in a manner such that it is completely intertwined with algorithms
commonly in use today, with an emphasis on graph and tree algorithms such as DFS and BFS. One of the primary goals
of this structure is to aid in the implementation of algorithms that can work with problems currently classified
as NP-Hard, while removing much of the tedium and the mathematics by embedding it into the data structure itself.
It is important to note that this data structure is not meant to serve the purpose of removing the high-level math
from commonly implemented algorithms, but rather to make it possible to dive much deeper into algorithms
and data-structures than has ever been managed in the past, by bringing the complex back into the realm of the simple,
allowing for seemingly simple tasks to be stacked on top of one another enough so that they again reach a level of
complexity such that they must undergo simplification once again.


ROOT NODE -->                                   *
                                                |
                                               / \
                                ______________/   \________________
                               /   \                           /   \
                    [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]
                         ______________/   \________________
                        /   \                           /   \
             [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]
                                /   \                           /   \
                     [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]     [U:L:V:R:D]

ALL NODES ALSO CONTAIN AN S-LINK

U: UPNODE --> U points towards the parent node
Format of the U-Node    [(Str)"Parent Node ID",
                         (Str) "Root-Node-ID",
                         (List) *Walk-Up path --> ["W1", "W2" ... "Wn"]]

L: LEFTNODE --> L points to the Node on the left and holds additional information
Format of the L-Node     [(Str) "Pointer to the left node of the node",
                          (Str) "Pointer to left node of Layer",
                          (Str) "Pointer to left node of branch"]

V: VALUENODE --> V points to the value contained within the node.

R: RIGHTNODE --> R points to the Node on the right and holds additional information
Format of the R-Node    [(Str) "Pointer to the right node of the node",
                         (Str) "Pointer to the right node of Layer",
                         (Str) "Pointer to the right node of the branch",
                         (List) *Walk-Right path --> ["W1", "W2" ... "Wn"]]

D: DOWNNODE --> D points downwards to the children nodes
Format of the R-Node    [(Bool) *Contains Children? "True/False", --> If False Thread to links
                         (List) *Children Node Keys --> ["K1", "K2", ... "Kn"]]

The ROOTNODE:
    Datatype:
        Contains multiple methods and is considered the controller of the function. Contains the walk-methods,
        as well as the walk algorithms.
"""

class Node(object):

    def __init__(self, parent, value, orient="RIGHT"):
        self.key = self._keygen(parent, orient)
        self.parent = [parent, "*", ["W1", "W2", "W3"]]   #Generates walk length by using regex expressions
        self.left = ["LEFT NODE ID", "LEFT-LAYER-ID", "LEFT-BRANCH-ID"]   #Linked list by layers and branches Lefts
        self.value = value
        self.right = ["RIGHT NODE ID", "RIGHT-LAYER-ID", "RIGHT-BRANCH-ID", ["W1", "W2", "W3"]] #Linked list Rights
        self.down = [False, ["FUTURE THREADS"]]     #If True, Children node keys, else, threading

    def _keygen(self, parent, orient):
        """
        Generates the key by analyzing the orientation and parent and inserting the node into the tree

        :param parent:
        :param orient:
        :return:
        """
        # First pull in the current linked-lists and link them directly so that they are mutable.

        # Second clone the list, run the procedure to rekey eveything

        # Finally Merge the update keys into the tree

        return "The Key"

class Root(object):

    def __init__(self):
        self.tree = []

    def make_children(self, parent, children):
        x = self.tree[parent]