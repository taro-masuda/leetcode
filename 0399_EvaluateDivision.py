class Solution:
    def dfs(self, equations, values, query) -> float:
        stack = []
        if query[0] not in self.dic or query[1] not in self.dic:
            return -1.0
        # below certainly has at least one elements
        if query[0] == query[1]:
            return 1
        visited = set()
        for elem1 in self.dic[query[0]]:
            if not elem1:
                continue
            stack.append((elem1,self.dic[query[0]][elem1]))
        while len(stack) > 0:
            cur = stack.pop(-1)
            visited.add(cur[0])
            if not cur:
                continue
            if len(cur) == 2:
                if cur[0] == query[1]:
                    return cur[1]
                else:
                    for nxt_node in self.dic[cur[0]]:
                        if (not nxt_node in visited) and nxt_node:
                            stack.append((nxt_node, self.dic[cur[0]][nxt_node]*cur[1]))
                continue
            for (nxt_point, nxt_value) in cur:
                if nxt_point == query[1]: # here is the end point!
                    return nxt_value
                else:
                    for nxt_node in self.dic[nxt_point]:
                        if not nxt_node in visited:
                            stack.append((nxt_node[0], nxt_node[1]*cur[1]))
        return -1.0
                    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answers = []
        self.dic = {}
        for i,eq in enumerate(equations):
            if not eq[0] in self.dic:
                se = {}
                se[eq[1]] = values[i]
                self.dic[eq[0]] = se
            else:
                self.dic[eq[0]][eq[1]] = values[i]
            if abs(values[i] - 0) > 1e-12:
                if not eq[1] in self.dic:
                    se = {}
                    se[eq[0]] = 1.0 / values[i]
                    self.dic[eq[1]] = se
                else:
                    self.dic[eq[1]][eq[0]] = 1.0 / values[i]
        for query in queries:
            ans = self.dfs(equations, values, query)
            answers.append(ans)
        return answers
