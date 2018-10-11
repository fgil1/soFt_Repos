#Uses python2.7
#Week 5 Algorithm on graphs - connecting points
	#Using a disjoin set for MST
#Franco Gil ~ Universidad de Carabobo - FaCyT

import sys
import math

def disjoint_set(less, n):
    a=0
    T=[]
    d=[-1]*n
    tempo=0
    while len(less) and a != n:
        u,v,w=less.pop(0)
        while d[u] > 0:
            u=d[u]
        while d[v] > 0:
            v=d[v]
        if u != v:
            #T.append((u,v,w)) # show the tree
            tempo+=w
            a+=1
            if d[v] <= d[u]:
                d[v]+=d[u]
                d[u]=v
            if d[u] < d[v]:
                d[u]+=d[v]
                d[v]=u
    return tempo

def w(a, b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    l=[]
    for i in range(n):
        u=(x[i], y[i]) # (x1, x2)
        for j in range(n):
            if i != j:
            	v=(x[j], y[j]) #(y1, y2)
                tri=( i, j, w(u, v) )
                l.append(tri)
    less = sorted( l, key = lambda l : l[2] )
    print("{0:.9f}".format(disjoint_set(less, n)))
