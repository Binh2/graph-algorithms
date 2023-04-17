import networkx as nx
from dijkstra import dijkstra 


def node_betweenness(G: nx.Graph):
  results = [ dijkstra(G, start_node) for start_node in G.nodes ]
  shortest_paths = { start_node: result[0] for start_node, result in zip(G.nodes, results) }
  distances = { start_node: result[1] for start_node, result in zip(G.nodes, results) }

  visited_path = []
  between = { node: 0 for node in G.nodes }
  for u in shortest_paths:
    for v in shortest_paths[u]:
      if {u, v} in visited_path or distances[u][v] <= 1:
        continue
      
      for shortest_path in shortest_paths[u][v]:
        number_of_shortest_paths = len(shortest_paths[u][v])
        for w in shortest_path[1:-1]:
          between[w] += 1/number_of_shortest_paths

      visited_path.append({u, v})
  return between


if __name__ == "__main__":
  from load_custom_graph import load_custom_graph
  G = load_custom_graph(1)
  print(node_betweenness(G))