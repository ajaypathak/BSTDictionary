import unittest
import pytest
from BST_Dictionary import BSTDictionary


class BST_DictionaryTestCase(unittest.TestCase):
    def test_insert_single_key(self):
        avl = BSTDictionary()
        # avl.insert(10,20)
        avl[10] = 20
        self.assertEqual(avl.root.key, 10)
        print(avl[10])
        avl[23] = "23 Value"
        print(avl[23])
        self.assertEqual(avl[23], "23 Value")

    def test_insert_empty_key(self):
        avl = BSTDictionary()
        with pytest.raises(ValueError):
            avl[None] = "Value 1"

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
            avl["abc"] = "abcvalue"
        with pytest.raises(ValueError):
            avl[0] = "0value"
        with pytest.raises(ValueError):
            avl[-1] = "negative key"
        with pytest.raises(ValueError):
            avl[""] = "Empty key"

    def test_search_nonexistent_key(self):
        avl = BSTDictionary(True)
        avl[1] = "Value 1"
        avl[11] = "Value 11"
        avl[12] = "Value 12"

        with pytest.raises(KeyError) as e:
            node = avl.search(40)
            print("Key not found")


if __name__ == '__main__':
    unittest.main()
