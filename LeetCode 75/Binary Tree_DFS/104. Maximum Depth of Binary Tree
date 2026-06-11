# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def __init__(self):
        self.max_d = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        # max_d = 0
        # count = 0
        # real_count = 0
        # tmp_count = 0
        # que = []
        # que.append(root)
        # node = que[0]
        # visited = [True]

        # while que:
        #     node = que[0]
        #     if node.left:
        #         que.append(node.left)
        #         tmp_count += 1
        #     if node.right:
        #         que.append(node.right)
        #         tmp_count += 1

        #     depth_reg += tmp_

        #     que.pop(0)

        
        
        def dfs(self, node, depth):
            if not node:
                return
            # print(depth, self.max_d)

            if self.max_d < depth:
                self.max_d = depth

            if node.left:
                dfs(self, node.left, depth+1)
            if node.right:
                dfs(self, node.right, depth+1)

        if not root:
            return 0

        dfs(self, root, depth)


        return self.max_d + 1
