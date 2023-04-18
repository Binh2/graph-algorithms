import networkx as nx
from matplotlib import pyplot as plt


def visualize_graph(G: nx.Graph, display_label=True):
  pos = nx.spring_layout(G)
  nx.draw_networkx_nodes(G, pos)
  if display_label: nx.draw_networkx_labels(G, pos)
  nx.draw_networkx_edges(G, pos)
  plt.show()


def visualize_graphs(Gs: list[nx.Graph], display_label=True):
  sizes = {
    1: {"nrows": 1, "ncols": 1},
    2: {"nrows": 2, "ncols": 1},
    3: {"nrows": 2, "ncols": 2},
    4: {"nrows": 2, "ncols": 2},
    5: {"nrows": 2, "ncols": 3},
    6: {"nrows": 2, "ncols": 3},
    7: {"nrows": 2, "ncols": 4},
    8: {"nrows": 2, "ncols": 4},
    9: {"nrows": 3, "ncols": 3},
  }
  fig, axes = plt.subplots(**sizes[len(Gs)])
  ax = axes.flatten()
  for i in range(len(Gs)):
    G = Gs[i]
    pos = nx.spring_layout(G)
    ax[i].set_xlabel(str(i+1))
    nx.draw_networkx_nodes(G, pos, ax=ax[i])
    if display_label: nx.draw_networkx_labels(G, pos, ax=ax[i])
    nx.draw_networkx_edges(G, pos, ax=ax[i])
  plt.show()