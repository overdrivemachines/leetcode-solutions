# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeWithoutRecursion(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # add the root to the queue
        nodes = []
        nodes.append(root)

        while nodes:
            node = nodes.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

