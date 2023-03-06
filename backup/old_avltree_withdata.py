from graphviz import Digraph
import time
import os
class Node:
    def __init__(self, key, data):
        if not isinstance(key, int) or key <= 0:
            raise ValueError("Key must be a positive integer")
        self.key = key
        self.data = data if data is not None else []
        self.height = 1
        self.left = None
        self.right = None

class BST_Dictionary:
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

    def insert(self, key, data):
        def _insert(node, key, data):
            if key is None:
                raise ValueError("Key cannot be none")
            if node is None:
                return Node(key, data)
            
            if key < node.key:
                node.left = _insert(node.left, key, data)
            elif key > node.key:
                node.right = _insert(node.right, key, data)
            else:
                # key already exists, raise an exception
                raise KeyError(f"Key '{key}' already exists in the Dictionary")
                

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

        self.root = _insert(self.root, key, data)

    def search(self, key):
        def _search(node, key):
            if node is None:
                return None
            if key == node.key:
                return node.data
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

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

        dot = Digraph(comment="AVL Tree")
        _print_tree(self.root, dot)
        dot.render(os.path.join('trees', fileName),view=True)
    
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

if __name__ == "__main__":
    # Create an instance of the AVL tree
   tree = BST_Dictionary()

   # Insert some data into the tree
   tree.insert(2, 20)
   tree.insert(4, 21)
   tree.insert(1, "w2w")
   tree.insert(20, ["happy", "sad"])
   tree.insert(99, "abc")
   tree.insert(32, ("a", 1, "b"))
   tree.insert(12, "xyz")
   
   try:
    tree.insert(-12, "xyz")
   except NameError:
    print(ValueError)

       
       
   
   timestr = time.strftime("%Y%m%d-%H%M%S")

   print(tree.keys())
   print(tree.values())

   #tree.print_tree(timestr)

