from BST_Dictionary import BSTDictionary
import time
if __name__ == "__main__":
    # Create an instance of the AVL tree
   tree = BSTDictionary()

   # Insert some data into the tree
   #tree.insert(2, 20)
   #tree.insert(4, 21)
   #tree.insert(1, "w2w")
   #tree.insert(20, ["happy", "sad"])
   #tree.insert(99, "abc")
   #tree.insert(32, ("a", 1, "b"))
   #tree.insert(12, "xyz")
   tree[2]=20
   tree[4]=21
   tree[1]="w2w"
   tree[20]=["happy", "sad"]
   tree[99]="abc"
   tree[32]=("a", 1, "b")
   tree[12]="xyz"


   tree.print_tree("__setItem()__")
   timestr = time.strftime("%Y%m%d-%H%M%S")

   print(tree.keys())
   print(tree.values())

   #tree.print_tree(timestr)
