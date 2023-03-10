import unittest
import pytest
from BST_Dictionary import BSTDictionary


class BST_DictionaryTestCase(unittest.TestCase):
    def test_insert_single_key(self):
        avl1 = BSTDictionary()
        
        avl1[10] = 20
        self.assertEqual(avl1.root.key, 10)
        print(avl1[10])
        avl1[23] = "23 Value"
        print(avl1[23])
        self.assertEqual(avl1[23], "23 Value")

    def test_insert_empty_key(self):
        avl2 = BSTDictionary()
        with pytest.raises(ValueError):
            avl2[None] = "Value 1"

    def test_avl_tree_duplicate_key_insertion(self):
        avl3 = BSTDictionary(False)
        avl3[1] = "Value 1"
        avl3[11] = "Value 11"
        avl3[12] = "Value 12"
        with self.assertRaises(KeyError):
            avl3[1] = "Value 2"

    def test_avl_tree_allow_duplicate_key_insertion(self):
        avl4 = BSTDictionary(True)
        avl4[1] = "Value 1"
        avl4[11] = "Value 11"
        avl4[12] = "Value 12"
        avl4[1] = "Value 2"
        self.assertEqual(avl4[1], "Value 2")

    def test_invalid_key(self):
        avl5 = BSTDictionary()
        with pytest.raises(ValueError):
            avl5["abc"] = "abcvalue"
        with pytest.raises(ValueError):
            avl5[0] = "0value"
        with pytest.raises(ValueError):
            avl5[-1] = "negative key"
        with pytest.raises(ValueError):
            avl5[""] = "Empty key"

    def test_search_nonexistent_key(self):
        avl6 = BSTDictionary(True)
        avl6[1] = "Value 1"
        avl6[11] = "Value 11"
        avl6[12] = "Value 12"

        keyPresent=avl6.containsKey(100)
        self.assertEqual(False,keyPresent)

        keyPresent=avl6.containsKey(1)
        self.assertEqual(True,keyPresent)

        with pytest.raises(KeyError) as e:
            node = avl6.search(40)
            print("Key not found")
    
    def test_delete(self):
        avl7 = BSTDictionary(True)
        numbers = [9, 5, 10, 20, 6, 11, 12, 1, 2]
        for num in numbers:
            avl7[num]=str(num)
        
        i=1
        
        numbers = [22]
        for num in numbers:
            avl7.delete(num)
            avl7.print_tree(str(i) + "_"+ str(num)+"_delete")
            i=i+1
    # def test_printDictionary(self):
    #     list=[64, 1, 14, 26, 13, 110, 98, 85]
    #     numberlist=[]
    #     bst = BSTDictionary(True)
    #     for num in list:
    #         key=num
    #         numberlist.append(key)
            
    #         value=num
    #         bst[key]=value
            
    #     bst.print_tree("input4")
    






if __name__ == '__main__':
    unittest.main()
