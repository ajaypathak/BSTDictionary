import unittest
import pytest
from  BST_Dictionary import BSTDictionary

class BST_DictionaryTestCase(unittest.TestCase):
    def test_insert_single_key(self):
        avl = BSTDictionary()
        #avl.insert(10,20)
        avl[10]=20
        self.assertEqual(avl.root.key, 10)
        print(avl[10])
        avl[23]="23 Value"
        print(avl[23])
        self.assertEqual(avl[23], "23 Value")
    
    def test_insert_empty_key(self):
        avl = BSTDictionary()
        with pytest.raises(ValueError):
            avl[None]="Value 1"
    
    def test_avl_tree_duplicate_key_insertion(self):
        avl = BSTDictionary(False)
        avl[1] = "Value 1"
        avl[11] = "Value 11"
        avl[12] = "Value 12"
        with self.assertRaises(KeyError):
             avl[1] = "Value 2"
    

    def test_avl_tree_allow_duplicate_key_insertion(self):
        avl = BSTDictionary(True)
        avl[1] = "Value 1"
        avl[11] = "Value 11"
        avl[12] = "Value 12"
        avl[1] = "Value 2"
        self.assertEqual(avl[1], "Value 2")

    
    def test_invalid_key(self):
        avl = BSTDictionary()
        with pytest.raises(ValueError):
            avl["abc"]="abcvalue"            
        with pytest.raises(ValueError):
            avl[0]="0value"
        with pytest.raises(ValueError):
            avl[-1]="negative key"
        with pytest.raises(ValueError):
            avl[""]="Empty key"

        



    # def test_insert_multiple_keys(self):
    #     avl = AVLTree()
    #     avl.insert(10)
    #     avl.insert(20)
    #     avl.insert(30)
    #     self.assertEqual(avl.root.key, 20)
    #     self.assertEqual(avl.root.left.key, 10)
    #     self.assertEqual(avl.root.right.key, 30)

    # def test_insert_duplicate_key(self):
    #     avl = AVLTree()
    #     avl.insert(10)
    #     avl.insert(20)
    #     avl.insert(10)
    #     self.assertEqual(avl.root.key, 10)
    #     self.assertEqual(len(avl.root.values), 2)

    # def test_search_existing_key(self):
    #     avl = AVLTree()
    #     avl.insert(10)
    #     avl.insert(20)
    #     avl.insert(30)
    #     node = avl.search(20)
    #     self.assertIsNotNone(node)
    #     self.assertEqual(node.key, 20)

    # def test_search_nonexistent_key(self):
    #     avl = AVLTree()
    #     avl.insert(10)
    #     avl.insert(20)
    #     avl.insert(30)
    #     node = avl.search(40)
    #     self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
