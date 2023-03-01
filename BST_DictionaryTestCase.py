import unittest
from  avltree_withdata import BST_Dictionary

class BST_DictionaryTestCase(unittest.TestCase):
    def test_insert_single_key(self):
        avl = BST_Dictionary()
        avl.insert(10,20)
        self.assertEqual(avl.root.key, 10)
    
    def test_insert_empty_key(self):
        avl = BST_Dictionary()
        with self.assertRaises(ValueError):
            avl.insert(None,23)
    
    def test_avl_tree_duplicate_key_insertion(self):
        avl_tree = BST_Dictionary()
        avl_tree.insert(1, 'value1')
        with self.assertRaises(KeyError):
             avl_tree.insert(1, 'value2')


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
