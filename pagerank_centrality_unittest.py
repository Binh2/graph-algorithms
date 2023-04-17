import unittest
import networkx as nx
from load_custom_graph import load_custom_graph


class Test(unittest.TestCase):
  def __init__(self, inp, out, function, decimal_places: int = 2):
    super(Test, self).__init__()
    self.input = inp
    self.output = out
    self.function = function
    self.decimal_places = decimal_places

  def setUp(self) -> None:
    self.G = load_custom_graph(self.input)
    return super().setUp()
  
  def runTest(self):
    features = self.function(self.G)
    # self.assertDictEqual(features, self.output)
    for node in self.output:
      self.assertAlmostEqual(features[node], self.output[node], self.decimal_places, f"\n{features}\n{self.output}")

def suite():
  from pagerank_centrality import pagerank_centrality

  suite = unittest.TestSuite()
  numbers_of_nodes = { i+1: len(load_custom_graph(i+1).nodes.keys()) for i in range(3) }
  known_values = [
    (1, { node: pagerank * numbers_of_nodes[1] for node, pagerank in nx.pagerank(load_custom_graph(1)).items() }),
    (2, { node: pagerank * numbers_of_nodes[2] for node, pagerank in nx.pagerank(load_custom_graph(2)).items() }),
    (3, { node: pagerank * numbers_of_nodes[3] for node, pagerank in nx.pagerank(load_custom_graph(3)).items() }),
    # (3, nx.pagerank(load_custom_graph(3)))
  ]

  functions = [pagerank_centrality]
  for function in functions:
    suite.addTests(Test(inp, out, function) for inp, out in known_values)
  return suite


if __name__ == "__main__":
  unittest.TextTestRunner().run(suite())