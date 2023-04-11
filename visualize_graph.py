import networkx as nx
from matplotlib import pyplot as plt


def visualize_graph(G: nx.Graph, display_label=True):
  pos = nx.spring_layout(G)
  nx.draw_networkx_nodes(G, pos)
  if display_label: nx.draw_networkx_labels(G, pos)
  nx.draw_networkx_edges(G, pos)
  plt.show()