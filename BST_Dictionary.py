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
    # The constructor method of BSTDictionary initializes the root node to None and allows duplicates by default.
    # The allow_duplicates parameter can be set to False to disallow nodes with duplicate keys
    def __init__(self, allow_duplicates=True):
        self.root = None
        self.allow_duplicates = allow_duplicates

    # Returns the heigh of given node
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # Calculate the balance factor for a given node. Balance Factor=Height(Left Sub Tree)- Height(Right Sub Tree)
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Performs Left Rotation
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_root.height = 1 + \
            max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    # Performs Right Rotation
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_root.height = 1 + \
            max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    # Perform Search for a given key and return associated Node data. If key is not found,"KeyError" is raised
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

    # Print graphical representaton of Tree. This method uses the Graphviz library to create a visualization of the tree in the form of PDF File.
    # Left Edges are represented in red color. Right Edges are reprented in Green Color.
    # All generated files are created in Tree folder. If output file is already present, it will delete the old file and create the new file.
    def print_tree(self, fileName):
        def _print_tree(node, dot):
            if node:
                dot.node(str(node.key), str(node.key) + ": " + str(node.data))
                if node.left:
                    dot.edge(str(node.key), str(node.left.key),
                             style="outline", fillcolor="red")
                if node.right:
                    dot.edge(str(node.key), str(node.right.key),
                             style="outline", fillcolor="green")
                _print_tree(node.left, dot)
                _print_tree(node.right, dot)

        if not os.path.exists('trees'):
            os.makedirs('trees')

        outputFilePath = os.path.join('trees', fileName)
        try:
            if os.path.exists(outputFilePath):
                os.remove(outputFilePath)
        except:
            print("Error while deleting file ", outputFilePath)

        #dot = Digraph(comment="AVL Tree")
        #_print_tree(self.root, dot)
        #dot.render(outputFilePath, view=False)

    # Returns list of keys
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

    # Returns List of Values
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

    # Sets the value in Dictionary for a Given Key
    def __setitem__(self, key, value):
        self.insert(key, value)

    # Returns the value for a given key, otherwise raises KeyError
    def __getitem__(self, key):
        return self._search(self.root, key)

    # Utility Method for inserting Key into Dictionary
    def insert(self, key, data):
        if not isinstance(key, int) or key < 0:
            raise ValueError("Key must be a positive integer")
        if self.root is None:
            self.root = Node(key, data)
        else:
            self.root = self._insert(key, data, self.root)

    def _insert(self, key, data, node):

        # Step 1: Perform insert operation like standard BST
        if node is None:
            return Node(key, data)

        if key < node.key:
            node.left = self._insert(key, data, node.left)
        elif key > node.key:
            node.right = self._insert(key, data, node.right)
        else:
            if (self.allow_duplicates == True):
                node.data = data
            else:
                # key already exists, raise an exception
                txt = "Key {keyvalue} already exists in the Dictionary!"
                raise KeyError(txt.format(keyvalue=key))

        # Step 2 : Calculate the height of the node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        # Step 3 : Cancluatet he balance Factor
        balance = self.get_balance(node)

        # Step 4 Now check if node is not balanced.
        # T1, T2, T3 and T4 sub tree.

        # Case 1 : Left Left , Perform Right Rotation.
        #                                                     
        #                                                      a                                      b 
        #                                                     / \                                   /   \
        #                                                    b   T4      Right Rotate (c)          a      c
        #                                                   / \          - - - - - - - - ->      /  \    /  \ 
        #                                                  c   T3                               T1  T2  T3  T4
        #                                                 / \
        #                                               T1   T2

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        # Case 2 : Right Right Case. Perform Left Rotation
        #                                                      c                                b
        #                                                     /  \                            /   \ 
        #                                                    T1   b     Left Rotate(c)       c      a
        #                                                   /  \   - - - - - - - ->         / \    / \
        #                                                  T2   a                          T1  T2 T3  T4
        #                                                 / \
        #                                               T3  T4
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Case 3 : Left Right, Perform double rotation
        #         c                               c                           a
        #        / \                            /   \                        /  \ 
        #       b   T4  Left Rotate (b)        a    T4  Right Rotate(c)    b      c
        #      / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        #    T1   a                          b    T3                    T1  T2 T3  T4
        #        / \                        / \
        #      T2   T3                    T1   T2        
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Case 4 : Right Left. Perform double rotation
        #     c                            c                            a
        #    / \                          / \                          /  \ 
        #  T1   b   Right Rotate (b)    T1   a      Left Rotate(c)   c      b
        #      / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
        #     a   T4                      T2   b                  T1  T2  T3  T4
        #    / \                              /  \
        #  T2   T3                           T3   T4
        #        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Returns True in case key is present otherwise false.
    def containsKey(self,key):
        try:
            self._search(self.root, key)
            return True
        except KeyError as ke:
            return False