# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        node = root 

        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    return
            elif node.val < val:
                if node.right:
                    node = node.right
                else:
                    return
            else:
                return node

            
