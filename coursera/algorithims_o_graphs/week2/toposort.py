# Uses python2.7 
# Week3 - Topological sort
# ~ Franco Gil, Universidad de Carabobo - FaCyT

import sys

# DFS
def toposort_in(adj, go, vis, q):
    t = adj[go-1]
    i = 0
    while i < len(t):
        x = t[i]; i+=1
        x += 1
        if (x-1) < n and vis[x-1] == False:
            vis[x-1]=True
            toposort_in(adj, x, vis, q)
            q.insert(0, x)
            #print x,

def toposort(adj, vis, n):
    q=[]
    for i in range(n):
        if vis[i] == False:
            vis[i]=True
            if len(adj[i]):
                toposort_in(adj, i+1, vis, q)
            #print i+1,
            q.insert(0, i+1)
    return q

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
    vis = [False]*n
    q=toposort(adj, vis, n)
    #print q
    for i in range(n):
        print q[i],
