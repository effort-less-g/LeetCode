# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    p_val, q_val = 0, 0
    p_flag = False
    q_flag = False

    def dfs(self, node):

        if not node:
            return

        # if self.p_flag and self.q_flag:
        #     return

        if node.val == self.p_val:
            self.p_flag = True
            
        if node.val == self.q_val:
            self.q_flag = True


        self.dfs(node.left)
        self.dfs(node.right)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.nodes = []

        self.p_val = p.val
        self.q_val = q.val

        # print(root.val, root.right, root.left)

        # print(root.val)

        while root:

            self.p_flag = False
            self.q_flag = False

            # print(root.val)

            if root.val == p.val or root.val == q.val:
                # print("WHAT", root.val)
                return root

            self.dfs(root.left)

            # print(self.p_flag, self.q_flag, self.p_i, self.q_i, self.nodes)

            if self.p_flag and not self.q_flag:
                return root
            if not self.p_flag and self.q_flag:
                return root
            
            if not self.p_flag and not self.q_flag:
                root = root.right
            else:
                root = root.left
        

