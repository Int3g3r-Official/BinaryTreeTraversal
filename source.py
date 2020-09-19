class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def PrintTree(self,traversalType):
        if traversalType == "preorder":
            return self.PreorderPrint(tree.root)
        elif traversalType == "inorder":
            return self.InorderPrint(tree.root)
        elif traversalType=="postorder":
            return self.PostorderPrint(tree.root)
        else:    
            print("Traversal type is not supported.")
    def PreorderPrint(self,start,traversal=""):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value)+" - ")
            traversal  = self.PreorderPrint(start.left,traversal)
            traversal  = self.PreorderPrint(start.right,traversal)
        return traversal
    def InorderPrint(self,start,traversal=""):
        # Left -> Root -> Right
        if start:
            traversal = self.InorderPrint(start.left,traversal)
            traversal +=(str(start.value)+" - ")
            traversal = self.InorderPrint(start.right,traversal)
        return traversal
    def PostorderPrint(self,start,traversal=""):
        # Left -> Right -> Root
        if start:
            traversal = self.PostorderPrint(start.left,traversal)
            traversal = self.PostorderPrint(start.right,traversal)
            traversal +=(str(start.value)+" - ")
        return traversal

        
#             1
#           /   \
#         2      3
#       /  \    / \
#      4    5  6  7


#Tree setup
tree                    = BinaryTree(1)
tree.root.left          = Node(2)
tree.root.right         = Node(3)
tree.root.left.left     = Node(4)
tree.root.left.right    = Node(5)
tree.root.right.left    = Node(6)
tree.root.right.right   = Node(7)

# Types of traversal(Depth-first order) : InOrder , PreOrder , PostOrder

print("              1")
print("           /    \\")
print("          2      3")
print("         / \    / \\")
print("        4   5  6   7")


print("PreOrder")
print(tree.PrintTree("preorder"))
print("InOrder")
print(tree.PrintTree("inorder"))
print("PostOrder")
print(tree.PrintTree("postorder"))