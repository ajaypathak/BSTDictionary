from BST_Dictionary import BSTDictionary
import time
if __name__ == "__main__":
    # Create an instance of the AVL tree
   tree = BSTDictionary()

   # Insert some data into the tree
   tree.insert(2, 20)
   tree.insert(4, 21)
   tree.insert(1, "w2w")
   tree.insert(20, ["happy", "sad"])
   tree.insert(99, "abc")
   tree.insert(32, ("a", 1, "b"))
   tree.insert(12, "xyz")
   
   try:
    tree.insert(12, "xyz")
  
   except KeyError as ke:
     print(ke)
   try:
    
    tree.insert(-12, "xyz")
   except ValueError as e:
    print(e)
   

       
       
   
   timestr = time.strftime("%Y%m%d-%H%M%S")

   print(tree.keys())
   print(tree.values())

   #tree.print_tree(timestr)
