class Solution:
    
    mp = {}
    visited = set()

    def dfs(self, node1, node2, m):
        # if node1 in self.visited:
        #     return
        # print(node1)
        self.visited.add(node1)
        # print(self.visited)
        
        # print(node1 in self.visited)

        ans = None

        for node, mult in self.mp[node1]:
            if node == node2:
                # print(m*mult, node)
                return m*mult
            # print(type(node), node, self.visited)
            # print(self.mp[node1])
            # print(node, mult, m, node2)
            # print(self.visited)
            if node in self.visited:
                # print("GGGGGG")
                continue
            # print(node, mult, m, node2)
            if node != node2:
                # print(node, mult, self.mp[node1])
                # self.visited.add(node)
                ans = self.dfs(node, node2, m*mult)
            if ans:
                return ans

        return None

    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        self.mp = {}


        for i, equation in enumerate(equations):
            if equation[0] not in self.mp:
                self.mp[equation[0]] = []
            if equation[1] not in self.mp:
                self.mp[equation[1]] = []
            self.mp[equation[0]].append((equation[1], values[i]))
            self.mp[equation[1]].append((equation[0], 1/values[i]))

        # print(self.mp)

        ans, res = None, []
        
        for node1, node2 in queries:
            
            self.visited = set()

            if node1 not in self.mp or node2 not in self.mp:
                res.append(-1)
                continue

            if node1 == node2:
                res.append(1)
                continue
    
            # self.visited.add(querie[0])
            # print(node1, node2, "\\\\\\\\\\\\\\\\\\\\\\\\")
            ans = self.dfs(node1, node2, 1)
            if ans:
                res.append(ans)
            else:
                res.append(-1)

        return res
