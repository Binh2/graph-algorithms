import networkx as nx


def degree_centrality(G: nx.Graph | nx.DiGraph):
  if type(G) == nx.Graph:
    return { node: len(G[node].keys()) for node in G.nodes }
  return { node: len(G[node].keys()) + len(list(G.predecessors(node))) for node in G.nodes}
