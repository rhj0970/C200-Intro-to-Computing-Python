
import random as rn

class Stack:
    def __init__(self):
        self.stack=[]
    def empty(self):
        return self.stack == []
    def pop(self):
        if not self.empty():
            return self.stack.pop(0)
    def push(self,x):
        self.stack.insert(0,x)
    def __str__(self):
        return str(self.stack)


class Queue:
    def __init__(self):
        self.queue = []
    def empty(self):
        return self.queue == []
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
    def enqueue(self,x):
        self.queue.append(x)
        return self
    def __str__(self):
        return str(self.queue)

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    def add_edge(self, pair):
        start,end = pair
        self.edges[start].append(end)
    def children(self,node):
        return self.edges[node]
    def nodes(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.edges)





def bfsfull(g,node):
    edge = g.edges
    visited = []
    que = Queue()
    que.enqueue(node)
    while not que.empty():
        Node = que.dequeue()
        if Node not in visited:
            print(Node)
            visited.append(Node)
            childlist = g.children(Node)
            for n in childlist:
                if n in g.nodes:
                    if n not in visited:
                        que.enqueue(n)
                else:
                    break
    
    unvisited = []
    for node in g.nodes:
        if node not in visited:
            unvisited +=[node]
    remaining = Graph(unvisited)
    for i in remaining.nodes:
        remaining.edges[i] = edge[i]
    if remaining.nodes != []:
        j = unvisited[rn.randrange(0,len(unvisited))]
        bfsfull(remaining, j)



g = Graph([1,2,3,4,5,6,7,8])
elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
for i in elst:
    g.add_edge(i)
print(g.edges)
bfsfull(g,5)
