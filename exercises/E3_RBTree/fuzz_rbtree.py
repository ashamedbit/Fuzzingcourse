from RBVerify import *
from generate_random_characters import *

trials = 1000

bst = RBTree()
bst_verify = RBVerify()

# Implement logic to fuzz the Red Black tree
# Can insert and delete numbers from the tree.

# How does the tree look after these insertions?
bst.print_tree()
# Verify assertions of Red Black tree
bst_verify.repOK(bst)