# Time Complexity : O(n), n is no of nodes in the tree
# Space Complexity : O(n), because the queue can store all leaf nodes at max in the worst case
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        # using bfs
        q = deque([root])

        x_found = False
        y_found = False

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr.left is not None and curr.right is not None:
                    if curr.left.val == x and curr.right.val == y:
                        # siblings
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False

                # if the current node has the either of the target values, we will update the respective found variable
                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False

        return False
