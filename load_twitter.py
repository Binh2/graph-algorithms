import networkx as nx
from betweenness_centrality import betweenness
from visualize_graph import visualize_graph

def load_twitter(filename: str = "twitter_combined.txt"):
  G = nx.DiGraph()
  with open(filename) as file:
    for line in file:
      G.add_edge(*[ int(num) for num in line.split(" ") ])
  
  return G


if __name__ == "__main__":
  G = load_twitter()
  # G = nx.DiGraph()
  # G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)])
  # visualize_graph(list(G.edges)[:100]) 
  print(betweenness(G))
