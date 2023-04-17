from timeit import timeit, Timer
from typing import List
from pagerank_centrality import pagerank_centrality
from load_custom_graph import load_custom_graph
from print_2darray import print_2darray
from constants import TIMING_NUMBER_OF_ITERATION as NUMBER_OF_ITERATION, TIMING_GS as Gs


functions = { "Normal method": pagerank_centrality }
timing_array = []
for i in range(len(Gs)):
  timing_array.append([])
  G = load_custom_graph(Gs[i])
  for j in range(len(functions)):
    method_name = list(functions.keys())[j]
    timing_array[i].append(timeit(
      'functions[method_name](G)', 
      "from __main__ import functions, i, G, method_name", 
      number=NUMBER_OF_ITERATION
    ))


print_2darray(
  timing_array, 
  [ method_name for method_name in functions ],
  [f"Graph {G_name}: " for G_name in Gs]
)