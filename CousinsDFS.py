# Time Complexity : O(n), n is no of nodes in the tree
# Space Complexity : O(h), because its a recusrive solution, stack takes h no of elements in worst case
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.x_parent = None
        self.y_parent = None
        self.x_lvl = -1
        self.y_lvl = -1
    
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        
        # using dfs
        self.dfs(root, -1, 1, x, y)
        if self.x_parent != self.y_parent and self.x_lvl == self.y_lvl:
            return True
        else:
            return False
        
    def dfs(self, root, parent, lvl, x, y):
            if root is None:
                return
            # using preorder traversal, we can use any
            if root.val == x:
                # x's parent is root's parent
                self.x_parent = parent
                self.x_lvl = lvl
            if root.val == y:
                # y's parent is root's parent
                self.y_parent = parent
                self.y_lvl = lvl
            # lvl increases, root becomes parent
            self.dfs(root.left, root, lvl+1, x, y)
            self.dfs(root.right, root, lvl+1, x, y)