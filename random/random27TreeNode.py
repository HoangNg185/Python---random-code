#creating a treenode, u can find sort order (inorder_traversal), insert new int into that treenode, find value, etc

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value <self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    def find(self, value):
        if value <self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
tree = TreeNode(10)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(56)
tree.insert(16)
tree.insert(12)

print(tree.left.right.value)
print('-----------')
print(tree.inorder_traversal())
print('-----------')
print(tree.preorder_traversal())
print('-----------')
print(tree.postorder_traversal())
print('-----------')
print(tree.find(6))
print(tree.find(8))