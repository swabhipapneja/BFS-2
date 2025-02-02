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
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        
        # using bfs, if a node is at size - 1 place in the queue
        # it means that it is the last node of that level
        # so we can add it to our result list

        result = []
        q = deque([root])

        while q:
            # taking size to distinguish levels
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                # if it is the last element of that level
                if i == size - 1:
                    result.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        
        return result


        