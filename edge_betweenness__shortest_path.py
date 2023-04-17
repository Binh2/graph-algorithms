import networkx as nx
from dijkstra import dijkstra 


def edge_betweenness(G: nx.Graph | nx.DiGraph):
  results = [ dijkstra(G, start_node) for start_node in G.nodes ]
  shortest_paths = { start_node: result[0] for start_node, result in zip(G.nodes, results) }
  distances = { start_node: result[1] for start_node, result in zip(G.nodes, results) }

  visited_path = []
  between = { edge: 0 for edge in G.edges }
  for u in shortest_paths:
    for v in shortest_paths[u]:
      if {u, v} in visited_path or distances[u][v] <= 0:
        continue
      
      for shortest_path in shortest_paths[u][v]:
        number_of_shortest_paths = len(shortest_paths[u][v])
        for i in range(len(shortest_path[:-1])):
          edge = (shortest_path[i], shortest_path[i+1])
          if edge not in between:
            edge = (shortest_path[i+1], shortest_path[i])
          between[edge] += 1/number_of_shortest_paths

      visited_path.append({u, v})
  return between

if __name__ == "__main__":
  from load_custom_graph import load_custom_graph
  G = load_custom_graph(1)
  print(edge_betweenness(G))