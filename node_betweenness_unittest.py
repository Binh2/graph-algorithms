import unittest
import networkx as nx
from load_custom_graph import load_custom_graph


class NodeBetweennessTest(unittest.TestCase):
  def __init__(self, inp, out, node_betweenness):
    super(NodeBetweennessTest, self).__init__()
    self.input = inp
    self.output = out
    self.node_betweenness = node_betweenness

  def setUp(self) -> None:
    self.G = load_custom_graph(self.input)
    return super().setUp()
  
  def runTest(self):
    between = self.node_betweenness(self.G)
    self.assertDictEqual(between, self.output)

def suite():
  from node_betweenness__shortest_path import node_betweenness as node_betweenness1

  suite = unittest.TestSuite()
  known_values = [
    (1, { 1: 0.0, 2: 1.5, 3: 1.0, 4: 4.5, 5: 3.0, 6: 0.0 }),
    (2, { 1: 3.0, 2: 0.0, 3: 3.0, 4: 15.0, 5: 6.0, 6: 6.0, 7: 7.0, 8: 0.0, 9: 0.0 }),
    (3, { 1: 0.0, 2: 1.5, 3: 1.5, 4: 6.0, 5: 0.0, 6: 0.0 }),
  ]

  functions = [node_betweenness1]
  for function in functions:
    suite.addTests(NodeBetweennessTest(inp, out, function) for inp, out in known_values)
  return suite


if __name__ == "__main__":
  # unittest.main()
  unittest.TextTestRunner().run(suite())