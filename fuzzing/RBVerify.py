from RBTree import *

# Define R-B Tree
class RBVerify():
    tree_depth = -1

    # Root is black and has no parent
    def root_assertion(self, root):
        assert root.color == 0
        assert root.parent == None

    # tree nodes are either red or black
    def red_black(self, root):
        if root == None:
            return
        assert root.color == 0 or root.color == 1
        self.red_black(root.left)
        self.red_black(root.right)

    # tree is acyclic
    def acyclic(self, root):
        visited = set()
        if root == None:
            return
        
        assert root not in visited
        visited.add(root)

        self.acyclic(root.left)
        self.acyclic(root.right)
    
    #  All leafs are black
    def leaf_is_black(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            assert root.color == 0
        self.leaf_is_black(root.left)
        self.leaf_is_black(root.right)

    # A red node cannot have a red node as a child
    def red_property(self, root):
        if root == None:
            return
        if root.color == 1:
            assert root.left is not None and root.left.color == 0
            assert root.right is not None and root.right.color == 0
        self.red_property(root.left)
        self.red_property(root.right)
    
    # Number of black nodes on each path from root to leaf is same
    def depth_property(self, root, depth):
        if root == None:
            return
        if root.color == 0:
            depth = depth + 1
        
        if root.left == None and root.right == None:
            # Set this static variable for first time
            if RBVerify.tree_depth == -1:
                RBVerify.tree_depth = depth
            assert RBVerify.tree_depth == depth
        self.depth_property(root.left, depth)
        self.depth_property(root.right, depth)

    def check_assertions(self, tree):
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


