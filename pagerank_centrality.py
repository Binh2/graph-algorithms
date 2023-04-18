import networkx as nx
from degree_centrality import degree_centrality
import math


def pagerank_centrality(G: nx.Graph | nx.DiGraph, damping_factor: float = 0.85, number_of_iterations: int = -1):
  pagerank = { node: 1 for node in G.nodes}
  out_degree = { node: len(G[node].keys()) for node in G.nodes}
  degree = degree_centrality(G)
  # print(out_degree)
  no_out_degree_nodes = [ node for node in G.nodes if out_degree[node] == 0 ]

  i = 0
  while True:
    sum_difference = 0
    if i != -1 and i < number_of_iterations:
      break
    temp_pagerank = { node: 0 for node in G.nodes }
    for u in G.nodes:
      for v in list(G.predecessors(u)) + no_out_degree_nodes if type(G) == nx.DiGraph else G[u]:
        # print(u, v, out_degree[v])
        if out_degree[v] != 0:
          temp_pagerank[u] += pagerank[v] / out_degree[v]
        else:
          temp_pagerank[u] += pagerank[v] / (len(G.nodes))
      temp_pagerank[u] = (1 - damping_factor) + damping_factor * temp_pagerank[u]
      sum_difference += abs(pagerank[u] - temp_pagerank[u])
    # print(temp_pagerank)
    if sum_difference <= 1e-9:
      break

    pagerank = temp_pagerank
    i += 1
  
  return pagerank

if __name__ == "__main__":
  # from load_custom_graph import load_custom_graph
  # print(pagerank_centrality(load_custom_graph(3)))
  from load_custom_graph import load_custom_graph
  from visualize_graph import *
  G = load_custom_graph(2)
  visualize_node_feature_graph(G, pagerank_centrality(G))