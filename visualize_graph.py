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


def visualize_node_feature_graphs(Gs: list[nx.Graph], features, display_label=True):
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
    visualize_node_feature_graph(G, features, display_label, ax=ax[i])
  plt.show()


def visualize_edge_feature_graphs(Gs: list[nx.Graph], features, display_label=True):
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
    visualize_edge_feature_graph(G, features, display_label, ax=ax[i])
  plt.show()



def visualize_node_feature_graph(G: nx.Graph | nx.DiGraph, features: dict, display_label: bool = True, ax = None):
  pos = nx.spring_layout(G)
  nx.draw(G, pos=pos, with_labels=display_label, ax=ax)
  nx.draw_networkx_labels(G, pos={node: (p[0]+.05, p[1]+.05) for node, p in pos.items()}, labels=features, ax=ax)
  plt.show()

def visualize_edge_feature_graph(G: nx.Graph | nx.DiGraph, features: dict, display_label: bool = True, ax = None):
  pos = nx.spring_layout(G)
  nx.draw(G, pos=pos, with_labels=display_label, ax=ax)
  edge_pos = {}
  shift = 0.01
  for edge in G.edges:
    edge_pos[edge] = ((pos[edge[0]][0] + pos[edge[1]][0])/2 + shift, (pos[edge[0]][1] + pos[edge[1]][1])/2 + shift)
  nx.draw_networkx_labels(G, pos=edge_pos, labels=features, ax=ax)
  plt.show()
