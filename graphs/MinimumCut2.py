import random, copy
from f_to_array import integer_rows_to_dict

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
    #    print "GRAPH:",G
        v1, v2 = choose_random_key(G)
    #    print "PICKED:",v1,v2
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1) 
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    #print "LENGTH:",length
    #print "FINISHED:",G,length
    return length[0]

g = integer_rows_to_dict("../inputs/min_cut_graph.txt")

print karger(g)
