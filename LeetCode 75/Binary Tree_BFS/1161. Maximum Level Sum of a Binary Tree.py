# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        que = [(root, 1)]
        counts = {}
        ans, max_val = 1, root.val 
        while que:

            # print(max_val)
            if que[0][0].left:
                que.append((que[0][0].left, que[0][1]+1))
            if que[0][0].right:
                que.append((que[0][0].right, que[0][1]+1))
            
            if que[0][1] not in counts:
                counts[que[0][1]] = que[0][0].val
            else:

                counts[que[0][1]] += que[0][0].val
            
            # print(counts[str(que[0][1])])

            # print(que[0][0].val, que[0][1])
        

            que.pop(0)

        for key in counts:
            if  counts[key] > max_val:
                ans = key
                max_val = counts[key]

        # print(counts)

        return ans

            
