# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:29:21 2017

@author: arnab
"""

import networkx as nx
import itertools as it
import matplotlib.pyplot as plt

# finds 2 communities in the given graph G
def detectCommunities(G):
    nodes = set(G.nodes())
    n = G.number_of_nodes()
    e = G.number_of_edges()

    first_community = []
    second_community = []
    clusters = set()
    # find all the possible combinations of nodes in communities c1 and c2
    # c1 = {1,2}, c2 = {3,4} is equivalent to c1 = {3,4}, c2 = {1,2}
    for i in range(1,n//2+1):
        for j in it.combinations(nodes,i):
            if j not in clusters:
                jcomplement = tuple(nodes - set(j))
                first_community.append(j)
                second_community.append(jcomplement)
                clusters.update([j, jcomplement])

    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = []
    # find the distrib of nodes in c1 and c2 that maximizes the ratio of intra-edges to inter-edges
    for i in range(len(first_community)):
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())
        num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i])
        ratio.append((float)((num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i]))

    maxIndex = ratio.index(max(ratio))
    print(first_community[maxIndex])
    print(second_community[maxIndex])

if __name__ == '__main__':
    G = nx.barbell_graph(4,0)
    nx.draw(G, with_labels=True)
    plt.show()
    detectCommunities(G)