from graphviz import Digraph
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data if data is not None else []
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
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

    def print_tree(self):
        def _print_tree(node, dot):
            if node:
                dot.node(str(node.key), str(node.key) + ": " + str(node.data))
                if node.left:
                    dot.edge(str(node.key), str(node.left.key), style="outline", fillcolor="red")
                if node.right:
                    dot.edge(str(node.key), str(node.right.key), style="outline", fillcolor="green")
                _print_tree(node.left, dot)
                _print_tree(node.right, dot)

        dot = Digraph(comment="AVL Tree")
        _print_tree(self.root, dot)
        dot.render(view=True)

if __name__ == "__main__":
    # Create an instance of the AVL tree
   tree = AVLTree()

   # Insert some data into the tree
   tree.insert(2, 20)
   tree.insert(4, 21)
   tree.insert(1, "w2w")
   tree.insert(20, ["happy", "sad"])
   tree.insert(99, "abc")
   tree.insert(32, ("a", 1, "b"))
   tree.insert(12, "xyz")
   tree.print_tree()


