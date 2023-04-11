import networkx as nx


def load_custom_graph(type: int):
  ''' type can be 1 or 2 '''
  G = nx.Graph()
  if type == 1:
    G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)])

  elif type == 2:
    G.add_edges_from([
      (1, 2), (1, 3), (1, 4),
      (2, 3),
      (3, 4),
      (4, 5), (4, 6),
      (5, 6), (5, 7), (5, 8),
      (6, 7), (6, 8),
      (7, 8), (7, 9),
    ])
  
  return G