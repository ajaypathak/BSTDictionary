from old_avltree import AVLTree

if __name__ == "__main__":
    avl_tree = AVLTree()

    # Insert keys into the AVL tree
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        avl_tree.insert(key)

    # Search for a key in the AVL tree
    search_key = 10
    node = avl_tree.search(search_key)
    if node:
        print(f"Found key {search_key} in the AVL tree")
    else:
        print(f"Could not find key {search_key} in the AVL tree")
    
    
    avl_tree.print_tree()
    # Delete a key from the AVL tree
    delete_key = 6
    avl_tree.delete(delete_key)

    # Print the AVL tree in-order traversal
    print("In-order traversal of the AVL tree:")
    avl_tree.in_order_traversal(avl_tree.root)
