# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:57:45 2019

@author: curaj
"""

import numpy as np
import networkx as net
def Graph(n,p):
    G=net.erdos_renyi_graph(n,p) 
    net.draw(G, with_labels=True)   
    Adj=net.adjacency_matrix(G).todense().astype(float)
    print(Adj)
    for i in range(Adj.shape[0]):
        sum=np.sum(Adj[i])
        if(sum!=0):
            Adj[i]=Adj[i]/np.sum(Adj[i])
    i_p=np.matrix([1/Adj.shape[0]]*Adj.shape[0])
    return (i_p,Adj)

def pageRank(i_p,t_p):
    p_i=i_p.dot(t_p)
    iterations=0
    error=np.sum(abs(p_i-i_p))
    while(error>0.01 and iterations<100):
        i_p=p_i
        p_i=p_i.dot(t_p)
        iterations=iterations+1
        error=np.sum(abs(p_i-i_p))
    return(p_i,error,iterations)
def modified_pageRank(i_p,t_p,c):
    p_i=c*(i_p.dot(t_p))+(1-c)*i_p
    iterations=0
    error=np.sum(abs(p_i-i_p))
    while(error>0.01 and iterations<100):
        i_p=p_i
        p_i=c*(i_p.dot(t_p))+(1-c)*i_p
        iterations=iterations+1
        error=np.sum(abs(p_i-i_p))
    return(p_i,error,iterations)
    
