from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')


# Creating Nodes
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# This represents:
#       10
#      /  \
#     5    15
#    / \     \
#   3   7     18
inorder(root)
print(f'\n')
preorder(root)
print(f'\n')
postorder(root)


class Solution:
    def inorderTra(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        return self.inorderTra(root.left) + [root.val] + self.inorderTra(root.right)


sol = Solution()
print(sol.inorderTra(root))
