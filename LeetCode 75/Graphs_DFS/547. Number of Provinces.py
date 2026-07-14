class Solution:
    isVisited = set()

    def traverse(self, node, isConnected):

        if node in self.isVisited:
            return
        
        self.isVisited.add(node)

        for j, num in enumerate(isConnected[node]):
            if j != node and num == 1:
                self.traverse(j, isConnected)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        size = len(isConnected)

        self.isVisited = set()
        # print(self.isVisited)
# 

        for i in range(size):
            # print(self.isVisited)
            if i not in self.isVisited:
                for j in range(size):
                    # print(isConnected[i][j])
                    if isConnected[i][j] == 1:
                        # print("asgas")
                        self.traverse(j, isConnected)
        #         # print("asgas")
                ans += 1



        # print(self.isVisited)
        # self.isVisted = set()


        return ans
