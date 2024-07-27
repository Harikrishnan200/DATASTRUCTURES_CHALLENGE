class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, current_node):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(key, current_node.left)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(key, current_node.right)
        else:
            print("Value already in tree!")

    def search(self, key):
        if self.root is not None:
            return self._search(key, self.root)
        else:
            return None

    def _search(self, key, current_node):
        if key == current_node.value:
            return current_node
        elif key < current_node.value and current_node.left is not None:
            return self._search(key, current_node.left)
        elif key > current_node.value and current_node.right is not None:
            return self._search(key, current_node.right)
        return None

    def delete(self, key):
        if self.root is not None:
            self.root = self._delete(key, self.root)

    def _delete(self, key, current_node):
        if current_node is None:
            return current_node

        if key < current_node.value:
            current_node.left = self._delete(key, current_node.left)
        elif key > current_node.value:
            current_node.right = self._delete(key, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_larger_node = self._min_value_node(current_node.right)
            current_node.value = min_larger_node.value
            current_node.right = self._delete(min_larger_node.value, current_node.right)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        elements = []
        if self.root is not None:
            elements = self._inorder_traversal(self.root)
        return elements

    def _inorder_traversal(self, current_node):
        elements = []
        if current_node.left is not None:
            elements += self._inorder_traversal(current_node.left)
        elements.append(current_node.value)
        if current_node.right is not None:
            elements += self._inorder_traversal(current_node.right)
        return elements

# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)

print("Inorder traversal:", bst.inorder_traversal())
print("Search for 7:", bst.search(7).value if bst.search(7) else "Not found")
bst.delete(10)
print("Inorder traversal after deleting 10:", bst.inorder_traversal())
