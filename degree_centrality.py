import networkx as nx


def degree_centrality(G: nx.Graph | nx.DiGraph):
  if type(G) == nx.Graph:
    return { node: len(G[node].keys()) for node in G.nodes }
  return { node: len(G[node].keys()) + len(list(G.predecessors(node))) for node in G.nodes}


if __name__ == "__main__":
  from load_custom_graph import load_custom_graph
  from visualize_graph import *
  G = load_custom_graph(2)
  visualize_node_feature_graph(G, degree_centrality(G))