class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data,curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)
        else:
            print("The node already exists in the BST")


    def delete(self,data):
        if self.root is not None:
            self._delete(data,self.root)
        else:
            print('BST is empty')

    def _delete(self, data, curr_node):
        if curr_node is None:
            return curr_node
        if data < curr_node.data:
            curr_node.left = self._delete(data,curr_node.left)
        elif data > curr_node.data:
            curr_node.right = self._delete(data,curr_node.right)
        else:
            if curr_node.left is None:
                return curr_node.right
            elif curr_node.right is None:
                 return curr_node.left

            min_value = self.min_value_node(curr_node.right)
            curr_node.data = min_value.data
            curr_node.right = self._delete(min_value.data, curr_node.right)
        return curr_node

    def min_value_node(self,curr_node):
        temp = curr_node
        while temp.left is not None:
            temp = temp.left
        return temp



    def search(self,key):
        if self.root is not None:
            return self._search(key,self.root)
        else:
            return None


    def _search(self,key,curr_node):
        if key == curr_node.data:
            return curr_node.data
        elif key < curr_node.data and curr_node.left is not None:
            return self._search(key,curr_node.left)
        elif key > curr_node.data and curr_node.right is not None:
            return self._search(key,curr_node.right)
        else:
            return None


    def inorder_traversal(self):
        # elements = []
        if self.root is not None:
            # elements = self._inorder_traversal(self.root)
            return self._inorder_traversal(self.root)
        # return self._inorder_traversal(self.root)


    def _inorder_traversal(self,curr_node):
        elements = []
        if curr_node.left is not None:
            elements += self._inorder_traversal(curr_node.left)
        elements.append(curr_node.data)
        if curr_node.right is not None:
            elements += self._inorder_traversal(curr_node.right)
        return elements


    def postorder_traversal(self):
        if self.root is not None:
            return self._postorder_traversal(self.root)
        else:
            return None   # Tree is empty
    def _postorder_traversal(self,curr_node):
        elements = []
        if curr_node.left is not None:
            elements += self._postorder_traversal(curr_node.left)
        if curr_node.right is not None:
            elements += self._postorder_traversal(curr_node.right)
        elements.append(curr_node.data)

        return elements

    def preorder_traversal(self):
        if self.root is not None:
            return self._preorder_traversal(self.root)
        else:
            return None

    def _preorder_traversal(self, curr_node):
        elements = []
        elements.append(curr_node.data)
        if curr_node.left is not None:
            elements += self._preorder_traversal(curr_node.left)
        if curr_node.right is not None:
            elements += self._preorder_traversal(curr_node.right)

        return elements

    def sum_of_all_nodes(self):
        if self.root is not None:
            return self._sum_of_all_nodes(self.root)
        else:
            return None


    def _sum_of_all_nodes(self, curr_node):
        if curr_node is None:
            return 0
        else:
            return curr_node.data + self._sum_of_all_nodes(curr_node.left) + self._sum_of_all_nodes(curr_node.right)

    def sum_of_leaf_nodes(self):
        if self.root is None:
            return None
        else:
            return self._sum_of_leaf_nodes(self.root)


    def _sum_of_leaf_nodes(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return current_node.data
        return self._sum_of_leaf_nodes(current_node.left) + self._sum_of_leaf_nodes(current_node.right)

    def count_leaf_nodes(self):
        if self.root is not None:
            return self._count_leaf_nodes(self.root)
        else:
            return None


    def _count_leaf_nodes(self, curr_node):
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return 1
        return self._count_leaf_nodes(curr_node.left) + self._count_leaf_nodes(curr_node.right)




bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)
bst.insert(7)

print(f"Searched element:{bst.search(5)}")
print(f"Inorder Traversal:{bst.inorder_traversal()}")
bst.delete(10)
print("After deleting Node 10")
print(f"Inorder Traversal:{bst.inorder_traversal()}")
print(f"Sum of all Nodes: {bst.sum_of_all_nodes()}")
print(f"Sum of leaf Nodes: {bst.sum_of_leaf_nodes()}")
print(f"Count of leaf Nodes: {bst.count_leaf_nodes() }")
print(f"Postorder Traversal:{bst.postorder_traversal()}")
print(f"Preorder Traversal:{bst.preorder_traversal()}")

