import networkx as nx


def load_twitter(filename: str = "twitter_combined.txt", number_of_edges = None):
  G = nx.DiGraph()
  if number_of_edges == None:
    with open(filename) as file:
      for line in file:
        G.add_edge(*[ int(num) for num in line.split(" ") ])
  else:
    i = 0
    with open(filename) as file:
      for line in file:
        if i >= number_of_edges:
          break
        G.add_edge(*[ int(num) for num in line.split(" ") ])
        i += 1
  
  return G


if __name__ == "__main__":
  from visualize_graph import visualize_graph
  from argparse import ArgumentParser
  argParser = ArgumentParser("Load twitter")
  argParser.add_argument("-n", "--number-of-edges", type=int, default=None)
  args = argParser.parse_args()
  G = load_twitter(number_of_edges=args.number_of_edges)
  visualize_graph(G)
