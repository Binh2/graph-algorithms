import networkx as nx


def pagerank_centrality(G: nx.Graph | nx.DiGraph, damping_factor: float = 0.85, number_of_iterations: int = 100):
  pagerank = { node: 1 for node in G.nodes}
  out_degree = { node: len(G[node].keys()) for node in G.nodes}
  # print(out_degree)

  for i in range(number_of_iterations):
    temp_pagerank = { node: 0 if len(G[node].keys()) > 0 else pagerank[node] for node in G.nodes }
    for u in G.nodes:
      for v in G.predecessors(u) if type(G) == nx.DiGraph else G[u]:
        if out_degree[v] != 0:
          temp_pagerank[u] += pagerank[v] / out_degree[v]
      temp_pagerank[u] = (1 - damping_factor) + damping_factor * temp_pagerank[u]
    # print(pagerank)
    pagerank = temp_pagerank
  
  return pagerank

if __name__ == "__main__":
  from load_custom_graph import load_custom_graph
  print(pagerank_centrality(load_custom_graph(3)))