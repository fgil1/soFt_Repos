#Uses python2
# Week 1
# ~Franco Gil, Universidad de Carabobo, Venezuela

import sys

def check_path( l, go ):
    """
    go: True, reverse then DFS
    go: False, no reverse then BFS 
    """
    x = 'B'
    if go:
        x = 'D'
    n = range(len(l))
    for i in n:
        l[i].sort(reverse = go)
    #print 'FS'

def dfs_in(adj, go, l, n):
    t = []
    if len(l) == 0:
        l.append(go)
    t = adj[go-1]
    while len(t) and len(l) < n:
        x = t[0]
        x += 1
        t.pop(0)
        if not x in l:
            l.append(x)
            dfs_in(adj, x, l, n)
    return l

def dfs_modf(adj, path, n ):
    part = path = []
    cc = 0
    size = 0
    for i in range(n):
        if not i+1 in path:
            path = dfs_in(adj, i+1, path, n)
            cc += 1
    return cc

# Working
def number_of_components(adj):
    path = []
    n  = len(adj)
    return dfs_modf(adj, path, n)

def reach(adj, a, b):
    part = path = []
    i = size = find = 0
    n = len(adj)
    while i < n and not find:
        if not i+1 in path:
            path = dfs_in(adj, i+1, path, n)
            if size < len(path):
            	start, end = size, len(path)
            	find = reach_in(path, a , b, start, end)
            	size = len(path)
        i += 1
    return find

def reach_in(path, a, b, start, end):
	i=0	# replace boolean 0 : False
	if a and b in path[start:end]:
		i=1
	return i

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x = data[-2] #
    y = data[-1] #
    #print x, y
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(number_of_components(adj))
    print reach(adj, x, y)
    
