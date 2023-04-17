from timeit import timeit, Timer
from typing import List
from node_betweenness__shortest_path import node_betweenness as node_betweenness1
from load_custom_graph import load_custom_graph
from print_2darray import print_2darray
from constants import TIMING_NUMBER_OF_ITERATION as NUMBER_OF_ITERATION, TIMING_GS as Gs


node_betweennesses = { "Shortest path method": node_betweenness1 }
timing_array = []
for i in range(len(Gs)):
  timing_array.append([])
  G = load_custom_graph(Gs[i])
  for j in range(len(node_betweennesses)):
    method_name = list(node_betweennesses.keys())[j]
    timing_array[i].append(timeit(
      'node_betweennesses[method_name](G)', 
      "from __main__ import node_betweennesses, i, G, method_name", 
      number=NUMBER_OF_ITERATION
    ))


print_2darray(
  timing_array, 
  [ method_name for method_name in node_betweennesses ],
  [f"Graph {G_name}: " for G_name in Gs]
)