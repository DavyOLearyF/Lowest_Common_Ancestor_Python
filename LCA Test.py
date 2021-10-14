import unittest
from Lowest_Common_Ancestor_Python import Node
from Lowest_Common_Ancestor_Python import findLCA
  
class LCATest(unittest.TestCase):
    
        #testing a normal case
    def test1(self): 
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 4, 5)
        assert lca == 2

        #testing the case when the root node is the LCA
    def test2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 1, 3)
        assert lca == 1

         #tests if LCA returns 1 of the nodes searched
    def test_case2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 2, 4)
        assert lca == 2
        
  
if __name__ == '__main__':
    unittest.main()