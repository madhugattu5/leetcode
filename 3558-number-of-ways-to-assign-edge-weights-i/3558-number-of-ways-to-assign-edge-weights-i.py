class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        queue = deque([(1, 0)])  
        visited.add(1)
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, depth + 1))
        k = max_depth
        return pow(2, k - 1, MOD)