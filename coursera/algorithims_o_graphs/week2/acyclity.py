# Uses python 2.7 
# Week2 acyclity
# Find a cycle in a graph
# Also, show information about the edges in the graph
# ~ Franco Gil Universidad de Carabobo- FaCyT

import sys

def DFS_counter_in(adj, go, find, n, count, counter, cycles = None,
        b=None, c=None, f=None):
    t = adj[go-1]
    i = 0
    while i < len(t):
        x = t[i]; i+=1
        x += 1
        if (x-1) < n and find[x-1] == False:
            find[x-1] = True
            if counter[1][x-1] == 0:
                counter[1][x-1] = count[0]; count[0] += 1
                counter[3][x-1] = count[1]; count[1] += 1
            DFS_counter_in(adj, x, find, n, count, counter, cycles, b, c, f)
            if counter[2][x-1] == 0:
                counter[2][x-1] = count[0]; count[0] += 1
            count[1] -= 1
        else:
            if cycles is not None:
                # back -condition 
                if counter[3][go-1] > counter[3][x-1]: # > distintos lvl
                    if b is not None and go > x and counter[2][go-1] == 0 and\
                        counter[2][x-1] == 0:
                        b.append([go,x]) # WORKIGN!
                    #forward-condition
                    if f is not None and go < x and counter[2][go-1] == 0:
                        f.append([go,x])
                else:
                    # cross-condition
                    if c is not None and go > x and \
                        counter[2][go-1] == 0 and counter[2][x-1] > 0:
                        c.append([go,x])

def DFS_counter(adj, cycles=None):
    n = len(adj)
    b=[]; c=[]; f=[] # > edges types to find!
    find =[False] * n
    counter=[[] for _ in range(4)] 
    count=[]; count.append(1); count.append(1) 
    for i in range(n):
        counter[0].append(i+1)
        counter[1].append(0)
        counter[2].append(0)
        counter[3].append(0)
    for i in range(n):
        if find[i] == False:
            find[i]=True
            if counter[1][i] == 0:
                counter[1][i] = count[0]; count[0] += 1
                counter[3][i] = count[1]; count[1] += 1
            DFS_counter_in(adj, i+1, find, n, count, counter, cycles, b, c ,f)
            if counter[2][i] == 0:
                counter[2][i] = count[0]; count[0] += 1
            count[1] -= 1
    if cycles==True:   
        if len(b) == 0:
            cycles_in = False
        else:
            cycles_in = True
        return cycles_in, None, None, None, None
    else: 
        return None, b, c, f, counter 

def DFS_counter_out(adj, cycles):
    print adj
    cyci, bi, ci, fi, counti = DFS_counter(adj, cycles)
    if cycles==True:
        return cyci
    else:
        return None, bi, ci, fi, counti

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
    cycles = False
    cycles=True
    info=False
    cyci=DFS_counter_out(adj, cycles)
    if cyci == True:
        print 1
    else:
        print 0
        if info:
            # > Informacion de G
            print 'back edges:   ', bi
            print 'cross-edge:   ', ci
            print 'forward-edge: ', fi
            print
            print 'vertices: ', counti[0]
            print 'inicio:   ', counti[1]
            print 'fin:      ', counti[2]
            print 'lvl:      ', counti[3]
