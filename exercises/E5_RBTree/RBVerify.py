from RBTree import *

# Define R-B Tree
class RBVerify():

    # Root is black and has no parent
    # Add code for this assertion
    def root_assertion(self, root):

    # tree nodes are either red or black
    # Add code for this assertion
    def red_black(self, root):

    # tree is acyclic
    # Add code for this assertion
    def acyclic(self, root):
    
    #  All leafs are black
    # Add code for this assertion
    def leaf_is_black(self, root):

    # A red node cannot have a red node as a child
    # Add code for this assertion
    def red_property(self, root):
    
    # Number of black nodes on each path from root to leaf is same
    # Add code for this assertion
    def depth_property(self, root, depth):

    def repOK(self, tree):
        root = tree.root
        #Insert code to check assertions below
        self.root_assertion(root)
        self.red_black(root)
        self.acyclic(root)
        self.leaf_is_black(root)
        self.red_property(root)
        RBVerify.tree_depth = -1
        self.depth_property(root, 0)
        return True


