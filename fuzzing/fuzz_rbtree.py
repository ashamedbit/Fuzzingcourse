from RBVerify import *
from generate_random_characters import *

trials = 1000

bst = RBTree()
bst_verify = RBVerify()

for i in range(trials):
    # Get a character stream which is of length 2. This is the value to insert into the tree
    data = int(fuzzer(2, ord('0') , 10))
    # Here we choose whether to insert or delete the value
    choice = int(fuzzer(1, ord('0') , 2))
    if choice == 0:
        bst.insertNode(data)
    else:
        bst.delete_node(data)

# How does the tree look after these insertions?
bst.print_tree()
# Verify assertions of Red Black tree
bst_verify.check_assertions(bst)