from random import randint
import matplotlib.pyplot as plt
import networkx as nx
import pydot
import graphviz
import pydot_ng as pydot
from graphviz import Digraph
import numpy as np
import pandas as pd

z0=pd.read_csv('edges2000.csv',sep=',',header=1)
zb=[]
for i in range(0,2090):
    zb.append((z[i][0],z[i][1]))
nx.Graph(edgelist)
plt.figure(figsize=(12,15))
nx.draw(H,node_size=25,node_color='yellow')
plt.savefig("SOCIAL_NETWORK_y.png")
plt.show()