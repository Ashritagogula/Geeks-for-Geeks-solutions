from collections import defaultdict, deque

class Solution:
    def maxEdgesToAdd(self, V, edges):
        adj = defaultdict(list)
        indeg = [0]*V
        
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        q = deque([i for i in range(V) if indeg[i] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        reachable = [set() for _ in range(V)]
        pos = {topo[i]: i for i in range(V)}

        for u in topo:
            for v in adj[u]:
                reachable[u].add(v)
                reachable[u] |= reachable[v]  # merge reachable of v into u

        total_possible = V * (V - 1) // 2
        existing_or_reachable = 0

        for i in range(V):
            existing_or_reachable += len(reachable[i])

        return total_possible - existing_or_reachable
