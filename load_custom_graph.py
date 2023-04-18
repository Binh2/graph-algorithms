import networkx as nx
from load_twitter import load_twitter


def load_custom_graph(type: int):
  ''' type can be 1 or 2 or 3. Type 1 and 2 are undirected graph. Type 3 is a directed graph '''
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
  elif type == 3:
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 2), (3, 4), (4, 5), (4, 6)])
  elif type == 11:
    G = load_twitter(number_of_edges=10)
  elif type == 12:
    G = load_twitter(number_of_edges=100)
  elif type == 13:
    G = load_twitter(number_of_edges=1000)
  elif type == 14:
    G = load_twitter(number_of_edges=10000)
  elif type == 15:
    G = load_twitter(number_of_edges=100000)
  elif type == 16:
    G = load_twitter(number_of_edges=1000000)
  elif type == 17:
    G = load_twitter()
  
  return G


if __name__ == "__main__":
  from visualize_graph import *
  from argparse import ArgumentParser
  argParser = ArgumentParser("Load custom graph")
  argParser.add_argument("-g", "--graphs", default=[1,2,3,11,12,13], nargs='+', type=int, help="Add the graph type here to display it")
  args = argParser.parse_args()
  if len(args.graphs) > 1:
    Gs = []
    for i in args.graphs:
      Gs.append(load_custom_graph(i))
    visualize_graphs(Gs)
  else:
    visualize_graph(load_custom_graph(args.graphs[0]))