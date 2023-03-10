class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            current = self.root
            while True:
                if key == current.key:
                    current.value = value
                    break
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, value)
                        break
                    else:
                        current = current.right

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key):
        parent = None
        current = self.root
        while current is not None:
            if key == current.key:
                if current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif current == parent.left:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif current == parent.left:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor_parent = current
                    successor = current.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current.key = successor.key
                    current.value = successor.value
                    if successor == successor_parent.left:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                return True
            elif key < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return False


    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, ":", node.value)
            self._inorder_traversal(node.right)

    def keys(self):
        keys_list = []
        self._keys(self.root, keys_list)
        return keys_list

    def _keys(self, node, keys_list):
        if node is not None:
            self._keys(node.left, keys_list)
            keys_list.append(node.key)
            self._keys(node.right, keys_list)

    def values(self):
        values_list = []
        self._values(self.root, values_list)
        return values_list

    def _values(self, node, values_list):
        if node is not None:
            self._values(node.left, values_list)
            values_list.append(node.value)
            self._values(node.right, values_list)
