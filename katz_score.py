import numpy as np
import networkx as nx
import math


def katz_centrality(G, alpha=0.1, beta=1,
          max_iter=1000, tol=1.0e-6,
          nstart=None, normalized=True,
          weight = 'weight'):
  result = np.array([1] * len(G.nodes))
  adj = nx.adjacency_matrix(G).todense()
  # print(adj)
  # print(np.matmul(adj * result[:, None]))
  for i in range(max_iter):
    # print(result)
    result = alpha * adj.dot(result) + beta
  # return { G.nodes[i]: result[i] for i in range(len(G.nodes))}

  s = 1
  if normalized:
    s = 1.0 / math.sqrt(sum(v**2 for v in result))
  result *= s
  return { node: result[i] for node, i in zip(G.nodes, range(10000000))}


def katz_score(G, beta = 0.5):
  '''KatzGF.
    beta: decaying factor default to 0.5
  '''
  katz_cen = nx.katz_centrality(G)

  # Calculate the KatzGF scores for all pairs of nodes
  katzgf_scores = {}
  for u in G.nodes():
    for v in G.nodes():
      if u != v and not G.has_edge(u, v):
        influence = 0.0
        for path in nx.all_simple_paths(G, source=u, target=v):
          path_length = len(path) - 1
          path_influence = 1.0
          for node in path[1:-1]:
            path_influence *= katz_cen[node]
          influence += beta**path_length * path_influence
        katzgf_scores[(u, v)] = influence

  return katzgf_scores


if __name__ == '__main__':
  import networkx as nx
  import math
  from load_custom_graph import load_custom_graph
  from visualize_graph import visualize_graph

  # G = nx.path_graph(4)
  G = load_custom_graph(21)
  visualize_graph(G)
  phi = (1+math.sqrt(5))/2.0 # largest eigenvalue of adj matrix
  # centrality = nx.katz_centrality(G,1/phi-0.01)
  # library_centrality = nx.katz_centrality(G)
  # self_centrality = katz_centrality(G)


  katz_scores = katz_score(G)
  
  # sort in descending order
  sorted_katz_scores = dict(sorted(katz_scores.items(), key=lambda item: item[1], reverse=True))

  # Print 100 first lines of scores
  for pair, score in list(sorted_katz_scores.items())[:100]:
    print(f"KatzGF score for {pair}: {score}")

  print("...")
  # Print 10 last lines of scores
  for pair, score in list(sorted_katz_scores.items())[len(list(katz_scores.items()))-11:]:
    print(f"KatzGF score for {pair}: {score}")

  # visual

  # print('node library self')
  # for n, c1, c2 in zip(library_centrality.keys(), library_centrality.values(), self_centrality.values()):
  #   # print(r1, r2)
  #   print("%d %0.7f %0.7f"%(n,c1, c2))

  # katz_scores = katz_score(G)