class Solution:
    def findOrder(self, n, prerequisites):
        from collections import defaultdict, deque
        adj=defaultdict(list)
        indegree=[0]*n
        for x,y in prerequisites:
            adj[y].append(x)
            indegree[x]+=1
        q=deque([i for i in range(n) if indegree[i]==0])
        order=[]
        while q:
            course=q.popleft()
            order.append(course)
            for next_course in adj[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        return order if len(order)==n else []
