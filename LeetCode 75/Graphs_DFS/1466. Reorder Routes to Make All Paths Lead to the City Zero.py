class Solution:
    nodemap = {}
    res = 0
    visited = set()

    def traverse(self, city):
        if city[0] in self.visited:
            return

        if city[1] == "out":
            self.res += 1

        self.visited.add(city[0])

        for citty in self.nodemap[city[0]]:
            self.traverse(citty)


    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.visited = set()
        self.visited.add(0)
        self.res = 0
        self.nodemap = {}
        
        for i in range(len(connections)):
            node1 = connections[i][0]
            node2 = connections[i][1]
            if node1 not in self.nodemap:
                self.nodemap[node1] = set()
            if node2 not in self.nodemap:
                self.nodemap[node2] = set()
            self.nodemap[node1].add((node2, "out"))
            self.nodemap[node2].add((node1, "in"))

        # print(self.nodemap)



        # print(self.nodemap[0])
    
        for city in self.nodemap[0]:
            self.traverse(city)

        return self.res

    
    # visited = set()
    # connections = []
    # res = 0

    # def traverse(self, node, idx):


    #     if node in self.visited:
    #         return
        
    #     # print(node)


    #     self.visited.add(node)

    #     if idx:
    #         self.res += 1

    #     for i in range(len(self.connections)):
    #         if node in self.connections[i]:
    #             if self.connections[i][0] == node:
    #                 self.traverse(self.connections[i][1], 1)
    #             else:
    #                 self.traverse(self.connections[i][0], 0)

    # def minReorder(self, n: int, connections: List[List[int]]) -> int:

    #     self.visited = set()
    #     self.visited.add(0)
    #     self.res = 0 
    #     self.connections = connections

    #     for i in range(len(connections)):

    #         if 0 in connections[i]:
    #             if connections[i][0] == 0:
    #                 self.traverse(connections[i][1], 1)
    #             else:
    #                 self.traverse(connections[i][0], 0)

    #     return self.res
