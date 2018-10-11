# use python 2.7
# Week 3 BFS
# Franco Gil, Universidad de Carabobo - FaCyT

import sys

def bfs_distance(adj, a, b):
    n=len(adj)
    lvl=[-1] * n; q=[] 
    lvl[a]=0 # root
    q.append(a)
    while len(q):
        u=q.pop(0)
        t=adj[u]
        for v in range(len(t)):
            x=t[v]
            if lvl[x] == -1:
                q.append(x)
                lvl[x] = lvl[u]+1
    if lvl[b] > 0:
        out=lvl[b]
    else:
        out=-1
    return out

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print bfs_distance(adj, s, t)
