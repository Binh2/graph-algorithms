import unittest
import networkx as nx
from load_custom_graph import load_custom_graph


class DegreeCentralityTest(unittest.TestCase):
  def __init__(self, inp, out, degree_centrality):
    super(DegreeCentralityTest, self).__init__()
    self.input = inp
    self.output = out
    self.degree_centrality = degree_centrality

  def setUp(self) -> None:
    self.G = load_custom_graph(self.input)
    return super().setUp()
  
  def runTest(self):
    between = self.degree_centrality(self.G)
    self.assertDictEqual(between, self.output)

def suite():
  from degree_centrality import degree_centrality

  suite = unittest.TestSuite()
  known_values = [
    (1, { 1: 2, 2: 3, 3: 2, 4: 3, 5: 3, 6: 1 }),
    (2, { 1: 3, 2: 2, 3: 3, 4: 4, 5: 4, 6: 4, 7: 4, 8: 3, 9: 1 }),
    (3, { 1: 2, 2: 3, 3: 3, 4: 4, 5: 1, 6: 1}),
  ]

  functions = [degree_centrality]
  for function in functions:
    suite.addTests(DegreeCentralityTest(inp, out, function) for inp, out in known_values)
  return suite


if __name__ == "__main__":
  unittest.TextTestRunner().run(suite())