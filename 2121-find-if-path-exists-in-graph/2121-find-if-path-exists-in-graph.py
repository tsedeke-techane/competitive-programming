class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)


        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        visited.add(source)

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    curr = dfs(adj)
                    if curr:
                        return True 
            return False

        return dfs(source)


            