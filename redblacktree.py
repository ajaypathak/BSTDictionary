class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            node.color = "black"
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current

            if node.value < current.value:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent is not None and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_left(node.parent.parent)

        self.root.color = "black"

    def rotate_left(self, node):
        y = node.right
        node.right = y.left

        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def rotate_right(self, node):
        y = node.left
        node.left = y.right

        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def search(self, value):

        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def print_tree(self):
        # Helper function to get the height of a tree
        def height(node):
            if node is None:
                return 0
            else:
                left_height = height(node.left)
                right_height = height(node.right)
                return max(left_height, right_height) + 1

        # Helper function to get the maximum width of a tree at a given level
        def max_width(node, level):
            if node is None:
                return 0
            elif level == 1:
                return 1
            else:
                left_width = max_width(node.left, level - 1)
                right_width = max_width(node.right, level - 1)
                return left_width + right_width

        # Get the height of the tree and the maximum width of each level
        tree_height = height(self.root)
        level_widths = [max_width(self.root, i)
                        for i in range(1, tree_height + 1)]

        # Calculate the total width of the tree
        total_width = sum(level_widths) + len(level_widths) - 1

        # Initialize an empty matrix to hold the tree
        tree_matrix = [[" " for _ in range(total_width)]
                       for _ in range(tree_height)]

        # Helper function to fill in the matrix with the values of the tree
        def fill_matrix(node, level, left, right):
            if node is None:
                return
            else:
                mid = (left + right) // 2
                tree_matrix[level][mid] = str(node.value)

                if node.color == "red":
                    tree_matrix[level][mid] = "\033[31m" + \
                        tree_matrix[level][mid] + "\033[0m"

                if node.left is not None:
                    fill_matrix(node.left, level + 1, left, mid - 1)

                if node.right is not None:
                    fill_matrix(node.right, level + 1, mid + 1, right)

        # Fill in the matrix with the values of the tree
        fill_matrix(self.root, 0, 0, total_width - 1)

        # Print the matrix row by row
        for row in tree_matrix:
            print(" ".join(row))


if __name__ == "__main__":
    rb_tree = RedBlackTree()

# Insert some values into the tree
    rb_tree.insert(2)
    rb_tree.insert(4)
    rb_tree.insert(1)
    rb_tree.insert(20)
    rb_tree.insert(90)
    rb_tree.insert(32)
    rb_tree.insert(12)

# Print the inorder traversal of the tree to show the values in sorted order
    # print("Inorder traversal of the Red-Black Tree: ")
    # rb_tree.inorder_traversal(rb_tree.root)
    rb_tree.print_tree()


# Search for a value in the tree
    value = 10
    if rb_tree.search(value):
        print(f"{value} is found in the tree.")
    else:
        print(f"{value} is not found in the tree.")
