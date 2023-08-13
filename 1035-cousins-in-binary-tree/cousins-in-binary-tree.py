# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xy = {x, y}

        if root is None:
            return False

        if root.left is not None and root.right is not None:
            if (root.left.val == x and root.right.val == y) or (
                root.left.val == y and root.right.val == x
            ):
                return False

        q = []
        q.append(root)

        while q:
            count = len(q)

            nodes = set()
            while count > 0:
                node = q.pop(0)
                # print(node.val, end=" ")

                nodes.add(node.val)
                child_values = set()
                if node.left:
                    q.append(node.left)
                    child_values.add(node.left.val)
                if node.right:
                    q.append(node.right)
                    child_values.add(node.right.val)

                if child_values == xy:
                    return False

                count -= 1

            # print(" ", nodes)

            if x in nodes and y in nodes:
                return True

        return False

