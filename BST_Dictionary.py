#from graphviz import Digraph

import os
class Node:
    def __init__(self, key, data):
        if not isinstance(key, int) or key <= 0:
            txt = "Key {keyvalue} must be a positive integer!"
            raise ValueError(txt.format(keyvalue=key))
        self.key = key
        self.data = data if data is not None else []
        self.height = 1
        self.left = None
        self.right = None

class BSTDictionary:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            raise KeyError("Key not found")

        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node.data

    def print_tree(self,fileName):
        def _print_tree(node, dot):
            if node:
                dot.node(str(node.key), str(node.key) + ": " + str(node.data))
                if node.left:
                    dot.edge(str(node.key), str(node.left.key), style="outline", fillcolor="red")
                if node.right:
                    dot.edge(str(node.key), str(node.right.key), style="outline", fillcolor="green")
                _print_tree(node.left, dot)
                _print_tree(node.right, dot)

        
        if not os.path.exists('trees'):
            os.makedirs('trees')

       # dot = Digraph(comment="AVL Tree")
       # _print_tree(self.root, dot)
       # dot.render(os.path.join('trees', fileName),view=True)
    
    def keys(self):
        keys = []

        def recursive_collect(node):
            if node is None:
                return

            recursive_collect(node.left)
            keys.append(node.key)
            recursive_collect(node.right)

        recursive_collect(self.root)
        return keys
    
    def values(self):
        data = []

        def recursive_collect(node):
            if node is None:
                return

            recursive_collect(node.left)
            data.append(node.data)
            recursive_collect(node.right)

        recursive_collect(self.root)
        return data
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        return self._search(self.root, key)
    
    def insert(self, key, data):
        if not isinstance(key, int) or key < 0:
            raise ValueError("Key must be a positive integer")
        if self.root is None:
            self.root = Node(key, data)
        else:
            self.root = self._insert(key, data, self.root)

    def _insert(self, key, data, node):
        if node is None:
            return Node(key, data)
        
        if key < node.key:
            node.left = self._insert(key, data,node.left)
        elif key > node.key:
            node.right = self._insert(key, data,node.right)
        else:
            # key already exists, raise an exception
            txt = "Key {keyvalue} already exists in the Dictionary!"
            raise KeyError(txt.format(keyvalue=key))

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
