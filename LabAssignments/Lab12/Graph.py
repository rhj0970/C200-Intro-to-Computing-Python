class Graph:
    """
    Graph Representation of class
    Created by Dr. D
    Modified by AIs
    """
    def __init__(self, nodes, directional):
        # FIXME: Can you make it so the class knows if it is a directional or bigraph when created?#
        self.nodes = nodes
        self.edges = {}
        self.directional = directional
        for i in self.nodes:
            self.edges[i] = []
        

    
    def add_edge(self, pair):
        
        """
        Adds an edge between the first node to 
        the second node in the list
        """
        start, end = pair
        self.edges[start].append(end)
        if self.directional == False:
            self.edges[end].append(start)
        # FIXME: Does the end node connect to the start node? (Refer to the first FIXME)
    
    def children(self, node):
        """
        Returns a list of all nodes attached to the node provided
        """
        # FIXME: What happens if the node is not in the graph?
        if self.edges[node] == 0:
            return []
        return self.edges[node]
    
    def dettachedNodes(self):
        """
        Returns a list of nodes have no edges
        """
        # TODO: Implement this to search the graph to find nodes with no edges
        dnode = []
        for i in self.edges:
            if self.edges[i] == 0:
                dnode += [i]
        return dnode
        # CHALLENGE: Can you make it for a directional graph to return nodes that have no edges COMING IN and leaving
    
    def __str__(self):
        finalString = ""
        for n in self.nodes:
            finalString += str(n) + " -> " + str(self.edges[n]) + "\n"
        return finalString
