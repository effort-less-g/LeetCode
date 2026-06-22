# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    ans = []

    def rec(self, node):

        if node.left:
            self.ans.append(self.rec(node.left))
            if node.right:
                self.ans.append(self.rec(node.right))
        elif node.right:
            self.ans.append(self.rec(node.right))
        else:
            print(node.val)
            return node.val
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        


        self.ans = []
        self.rec(root1)
        ans1 = self.ans
        self.ans = []
        self.rec(root2)
        
        if not root1.left and not root1.right:
            ans1 = [root1.val]

        if not root2.left and not root2.right:
            self.ans = [root2.val]

        ans1 = [x for x in ans1 if x is not None]
        self.ans = [x for x in self.ans if x is not None]


        print(ans1, self.ans)

        if ans1 == self.ans:
            return True
        
        return False


        # que1, ans1 = [], []
        # que1.append(root1)
        # while que1:
        #     node = que1[0]
        #     que1.pop(0)
        #     if node.left:
        #         que1.append(node.left)
        #     else:
        #         ans1.append(node.val) 
        #     if node.right:
        #         que1.append(node.right)
        #     else:
        #         ans1.append(node.val)
        
        # que2, ans2 = [], []
        # que2.append(root2)
        # while que2:
        #     node = que2[0]
        #     que2.pop(0)
        #     if node.left:
        #         que2.append(node.left)
        #     else:
        #         ans2.append(node.val) 
        #     if node.right:
        #         que2.append(node.right)
        #     else:
        #         ans2.append(node.val)

        # print(ans1, ans2)

        
