class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.key:
                root.left = self._insert(root.left, key)
            elif key > root.key:
                root.right = self._insert(root.right, key)
        return root
        
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example usage
# Initializing
bst = BinarySearchTree()

# Inserting
key = 10
bst.insert(key)
print(f"{key} inserted in the BST.")

# Searching
result = bst.search(key)
if result:
    print(f"{key} found in the BST.")
else:
    print(f"{key} not found in the BST.")

# Deleting
bst.delete(key)
print(f"{key} deleted from the BST.")