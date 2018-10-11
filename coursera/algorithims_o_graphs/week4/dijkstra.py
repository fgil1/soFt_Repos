# Uses python2.7 
# Week 4: Shortest path between v. s and v. t. Dijkstra algorithm
# Franco Gil ~ Universidad de Carabobo - FaCyT

import sys

def get_min(dist, find):
	x = 999999999 # inf
	go=False; i=0; pos=0
	while i < len(dist) and not go:
		if not find[i] and dist[i] < x:
			x = dist[i]
			pos=i
		i+=1
	return pos

def dijkstra(adj, cost, go, end=None):
	find=[False]*n
	dist=[99999999]*n
	dist[go]=0;
	k = 0
	while k<len(adj):
		go = get_min(dist, find) # O(N) 1st. iteration root
		if not find[go]:
			find[go]=True
			t=adj[go]; t_c=cost[go] # relaxing v. and hims cost
			i=0
			u=go # source
			while i<len(t):
				v=t[i]
				if dist[v] > dist[u]+t_c[i]:
					dist[v]=dist[u]+t_c[i]
				i+=1
		k+=1
	if dist[end]==99999999:
		print -1
	else:
		print dist[end]

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
    s, t = data[0] - 1, data[1] - 1
    dijkstra(adj, cost, s, t)
