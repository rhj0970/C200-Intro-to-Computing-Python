import numpy as np

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    def add_edge(self, pair):
        start,end = pair
        if start not in self.nodes:
            self.add_node(start)
            self.edges[start].append(end)
            return 1
        else:
            if end not in self.edges[start]:
                self.edges[start].append(end)
                return 1
            else:
                return -1
    def children(self,node):
        return self.edges[node]

    def reachable(x,y):
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
            return a
        
    if self.edges[x] == self.edges[y]:
        return True
    else:
        return False
        #Add a method reachable(x,y) that returns True if there exists a path from node x tonode y, and False
        # if no path exists. 
        #Use the transitive closure operation to determinethis.  
        #You can use the numpy dot method or use your own matrix multiplicationfunction you previously wrote.
            


    def nodes(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.edges)

    def add_node(n):
        if n not in self.nodes:
            self.nodes.append(n)
            return 1
        else:
            return -1

    def del_node(n):
        if n in self.edges:
            self.edges[n].remove(n)
            self.nodes.remove(n)
            
            return 1
        else:
            return -1


    
    def del_edge(x,y):
        if x in self.edges:
            self.edges[x].remove(x)
            self.edges[y].remove(y)
            return 1
        else:
            return -1
    
        








a = np.zeros ((4,4),dtype = int)
a[0][1] = 1
a[1][2] = 1
a[2][3] = 1
print(a)
a = np.dot (a,a) + a
print(a)
a = np.dot (a,a) + a
print(a)

for i in range(0,4):
    for j in range(0,4):
        if not i == j:
            print("{0} reaches {1}: {2}".format(i+1,j+1,bool(a[i][j])))