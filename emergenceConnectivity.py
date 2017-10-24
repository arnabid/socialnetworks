# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 17:28:05 2017

@author: arnab
"""

"""
The number of edges(added randomly) it takes on average to make a graph with n nodes
connected in nlogn
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy

# add 'n' nodes in a graph
def add_nodes(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

# add one random edge
def add_random_edge(G):
    v1,v2 = random.sample(G.nodes(), 2)
    G.add_edge(v1, v2)
    return G

# keeps adding random edges in G till it becomes connected
def add_till_connectivity(G):
    while not nx.is_connected(G):
        G = add_random_edge(G)
    return G

# takes input as number of nodes and returns number of nodes needed to make a connected graph
def create_instance(n):
    G = add_nodes(n)
    G = add_till_connectivity(G)
    return G.number_of_edges()

# average the graph over 50 instances
def create_avg_instance(n):
    list1 = []
    for i in range(0, 50):        
        list1.append(create_instance(n))
    return numpy.average(list1)

# plot the desired number of edges for connected graph
def plot_connectivity():
    x = []
    y_nedges = []
    y = []
    # 'i' is number of nodes
    i = 10
    while(i <= 300):
        x.append(i)
        y_nedges.append(create_avg_instance(i))
        y.append(i*numpy.log(i))
        i = i+10
    plt.xlabel('Number of nodes')
    plt.ylabel('Number of edges required to make the graph connected')
    plt.title('Emergence of connectivity')
    plt.plot(x, y)
    plt.plot(x, y_nedges)
    plt.show()

if __name__ == '__main__':
    plot_connectivity()
