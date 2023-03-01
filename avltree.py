# from graphviz import Digraph
# class AVLNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.height = 1
#         self.data=""

# class AVLTree:
#     def __init__(self):
#         self.root = None

#     def get_height(self, node):
#         if not node:
#             return 0
#         return node.height

#     def get_balance(self, node):
#         if not node:
#             return 0
#         return self.get_height(node.left) - self.get_height(node.right)

#     def right_rotate(self, node):
#         left_child = node.left
#         left_right_child = left_child.right

#         left_child.right = node
#         node.left = left_right_child

#         node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
#         left_child.height = max(self.get_height(left_child.left), self.get_height(left_child.right)) + 1

#         return left_child

#     def left_rotate(self, node):
#         right_child = node.right
#         right_left_child = right_child.left

#         right_child.left = node
#         node.right = right_left_child

#         node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
#         right_child.height = max(self.get_height(right_child.left), self.get_height(right_child.right)) + 1

#         return right_child

#     def insert(self, key):
#         def _insert(node, key):
#             if not node:
#                 return AVLNode(key)

#             if key < node.key:
#                 node.left = _insert(node.left, key)
#             elif key > node.key:
#                 node.right = _insert(node.right, key)
#             else:
#                 return node

#             node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

#             balance = self.get_balance(node)

#             if balance > 1 and key < node.left.key:
#                 return self.right_rotate(node)

#             if balance < -1 and key > node.right.key:
#                 return self.left_rotate(node)

#             if balance > 1 and key > node.left.key:
#                 node.left = self.left_rotate(node.left)
#                 return self.right_rotate(node)

#             if balance < -1 and key < node.right.key:
#                 node.right = self.right_rotate(node.right)
#                 return self.left_rotate(node)

#             return node

#         self.root = _insert(self.root, key)

#     def delete(self, key):
#         def _delete(node, key):
#             if not node:
#                 return node

#             if key < node.key:
#                 node.left = _delete(node.left, key)
#             elif key > node.key:
#                 node.right = _delete(node.right, key)
#             else:
#                 if not node.left:
#                     temp = node.right
#                     node = None
#                     return temp
#                 elif not node.right:
#                     temp = node.left
#                     node = None
#                     return temp

#                 temp = self.get_min_node(node.right)
#                 node.key = temp.key
#                 node.right = _delete(node.right, temp.key)

#             if not node:
#                 return node

#             node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

#             balance = self.get_balance(node)

#             if balance > 1 and self.get_balance(node.left) >= 0:
#                 return self.right_rotate(node)

#             if balance < -1 and self.get_balance(node.right) <= 0:
#                 return self.left_rotate(node)

#             if balance > 1 and self.get_balance(node.left) < 0:
#                 node.left = self.left_rotate(node.left)
#                 return self.right

#     def search(self, key):
#         def _search(node, key):
#             if not node:
#                 return None
#             if node.key == key:
#                 return node
#             if node.key > key:
#                 return _search(node.left, key)
#             return _search(node.right, key)

#         return _search(self.root, key)

#     def print_tree(self):
#         def _print_tree(node, dot):
#             if node:
#                 dot.node(str(node.key), str(node.key))
#                 if node.left:
#                     dot.edge(str(node.key), str(node.left.key))
#                 if node.right:
#                     dot.edge(str(node.key), str(node.right.key))
#                 _print_tree(node.left, dot)
#                 _print_tree(node.right, dot)

#         dot = Digraph(comment="AVL Tree")
#         _print_tree(self.root, dot)
#         dot.render(view=True)
        

# if __name__ == "__main__":
#     avl_tree = AVLTree()

#     # Insert keys into the AVL tree
#     keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
#     for key in keys:
#         avl_tree.insert(key)
        

#     # Search for a key in the AVL tree
#     search_key = 10
#     node = avl_tree.search(search_key)
#     if node:
#         print(f"Found key {search_key} in the AVL tree")
#     else:
#         print(f"Could not find key {search_key} in the AVL tree")
    
    
#     avl_tree.print_tree()
#     # Delete a key from the AVL tree
#     delete_key = 6
#     avl_tree.delete(delete_key)

#     # Print the AVL tree in-order traversal
#     print("In-order traversal of the AVL tree:")
#     avl_tree.in_order_traversal(avl_tree.root)
