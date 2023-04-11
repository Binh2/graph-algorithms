from typing import Any
import networkx as nx

def dijkstra(G: nx.Graph, start_node: Any) -> tuple[dict[Any, list[list[Any]]], dict[Any, int]]:
  '''
Input: 
  G: a undirected unweighted graph (created using networkx)
  start_node: a node to start from

Output:
  shortest_paths: a dictionary of all shortest possible paths (each path is a list)
  distances: a dictionary of distance

Example input:
  G = nx.Graph()
  G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)])
  start_node = 2
  from pprint import pprint
  pprint(dijkstra(G, start_node))

Example output:
  ({1: [[2, 1]],                        # all shortest paths from 2 to 1
  2: [[2]],                             # all shortest paths from 2 to 2
  3: [[2, 3]],                          # all shortest paths from 2 to 3
  4: [[2, 3, 4], [2, 5, 4]],            # all shortest paths from 2 to 4
  5: [[2, 5]],                          # all shortest paths from 2 to 5
  6: [[2, 3, 4, 6], [2, 5, 4, 6]]},     # all shortest paths from 2 to 6
 {1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 3})  # distances
  '''
  visited_node = []
  distances = {start_node: 0}
  shortest_paths = {start_node: [[start_node]]}
  
  for node in G.nodes:
    if node == start_node:
      continue
    distances[node] = len(G.nodes) - 1

  while len(visited_node) != len(G.nodes):
    not_visited_node = set(distances.keys()) - set(visited_node)
    min_distance_node = next(iter(not_visited_node))
    min_distance = distances[min_distance_node]
    for node in not_visited_node:
      if node in visited_node:
        continue

      distance = distances[node]
      if min_distance > distance:
        min_distance = distance
        min_distance_node = node
    

    for neighbor_node in G.adj[min_distance_node]:
      if distances[min_distance_node] + 1 < distances[neighbor_node]:
        distances[neighbor_node] = distances[min_distance_node] + 1
        
        shortest_paths[neighbor_node] = [shortest_path + [neighbor_node] for shortest_path in shortest_paths[min_distance_node]]
      
      elif distances[min_distance_node] + 1 == distances[neighbor_node]:
        for shortest_path in [shortest_path + [neighbor_node] for shortest_path in shortest_paths[min_distance_node]]:
          shortest_paths[neighbor_node].append(shortest_path)

    visited_node.append(min_distance_node)
  return shortest_paths, distances


if __name__ == "__main__":
  from load_custom_graph import load_custom_graph
  from pprint import pprint


  G = load_custom_graph(2)
  pprint(dijkstra(G, 2))