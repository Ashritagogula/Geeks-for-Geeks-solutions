class Solution:
    def safeNodes(self, V, edges):
        from collections import deque
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
        rev_graph = [[] for _ in range(V)]
        indegree = [0] * V
        for u in range(V):
            for v in graph[u]:
                rev_graph[v].append(u)
                indegree[u] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        safe = []
        while q:
            node = q.popleft()
            safe.append(node)
            for neigh in rev_graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        safe.sort()
        return safe
