class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)

        # step 2 : i'll count visited nodes
        visited = set()

    # step 3 : dfs function
        def dfs(node) :
            visited.add(node)
            for neighbour in graph[node] :
                if neighbour not in visited :
                    dfs(neighbour)

    # step 4 : Count connected Components
        components = 0
        for node in range(n) :
            if node not in visited :
                components += 1
                dfs(node)
    
        return components
    