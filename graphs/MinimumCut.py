import random

input = {"a":"bcd","c":"ae","b":"ad","d":"abe","e":"dc"}

class MinimumCut():
    def __init__(self,graph):
        self.graph = graph
        self.start = "d"
        self.vertex = self.graph[self.start]
        self.remaining_edges = self.vertex
        self.vertices = len(self.graph)
#        print self.graph
        while self.vertices > 2:
            print self.graph
            edge = self.pick_edge()
#            print "Chose:" + edge
            self.contract_vertices(edge)
            self.remove_self_loops(edge)
            self.vertices = len(self.graph)
            self.vertex = ''.join(set(self.vertex)).replace(self.start,"")
            self.remaining_edges = self.vertex
#            print self.vertex
#            print self.graph
        print self.graph

    def pick_edge(self):
        return random.choice(self.remaining_edges)

    def contract_vertices(self,edge):
#        self.vertex = self.vertex + self.graph[edge]
        self.graph[self.start+edge] = self.vertex + self.graph[edge]
        del self.graph[self.start]
        self.start = self.start + edge
        return

    def remove_self_loops(self,edge):
        if edge in self.vertex:
            self.vertex = self.vertex.replace(edge,"")
#            print "Removed edge: " + edge, self.vertex
        for i in self.graph.keys():
            if edge in self.graph[i]:
                self.graph[i] = self.graph[i].replace(edge,"")
        self.graph.pop(edge)
        return

MinimumCut(input)
