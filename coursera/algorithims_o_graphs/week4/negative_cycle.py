# Uses python2.7 
# Week 4: negative-cycle, implementing Bellman-Ford Algorithm
# Franco Gil ~ Universidad de Carabobo - FaCyT
import sys

def neg_cycle(adj, cost, root):
	n=len(adj)
	vis=[0]*n
	ant=[-1]*n 			
	dist=[float('inf')]*n
	dist[root]=0
	for i in range(len(adj)):
		for u in range(len(adj)):
			t=adj[u]; t_c=cost[u]
			for j in range(len(t)):
				v=t[j]; w=t_c[j] #: peso
				ant[u]=v
				if dist[v] > dist[u]+w:
					dist[v]=dist[u]+w
					if i == n-1:
						return 1
				elif dist[u]==float('inf') and dist[u]==dist[v]:
					dist[u]=0 # new root!
					dist[v]=dist[u]+w
	print 'ant: ', ant
	print 'dist: ', dist
	return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s=data[0]-1
    for i in range(n):
    	print 'inicio: ', i+1
    	print neg_cycle(adj, cost, i)
