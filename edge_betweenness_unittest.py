import unittest
import networkx as nx
from load_custom_graph import load_custom_graph


class EdgeBetweennessTest(unittest.TestCase):
  def __init__(self, inp, out, edge_betweenness):
    super(EdgeBetweennessTest, self).__init__()
    self.input = inp
    self.output = out
    self.edge_betweenness = edge_betweenness
    self.G = load_custom_graph(self.input)
  
  def runTest(self):
    between = self.edge_betweenness(self.G)
    if type(self.G) == nx.DiGraph:
      self.assertDictEqual(between, self.output)
    else:
      for edge in self.output:
        try:
          between[edge]
          self.assertAlmostEqual(between[edge], self.output[edge], msg=f'Betweenness of edge {edge} is not correct')
        except KeyError:
          try:
            reverse_edge = (edge[1], edge[0])
            self.assertAlmostEqual(between[reverse_edge], self.output[edge])
          except KeyError:
            self.fail(f'Edge {edge} does not exist')


def suite():
  from edge_betweenness__girvan_newman import edge_betweenness as edge_betweenness1
  from edge_betweenness__shortest_path import edge_betweenness as edge_betweenness2

  suite = unittest.TestSuite()
  known_values = [
    (1, { (1, 2): 2.0, (1, 5): 3.0, (2, 3): 3.5, (2, 5): 2.5, (3, 4): 3.5, (4, 5): 5.5, (4, 6): 5.0 }),
    (2, { (1, 2): 4.0, (1, 3): 1.0, (1, 4): 9.0, (2, 3): 4.0, (3, 4): 9.0, (4, 5): 10.0, (4, 6): 10.0, (5, 6): 1.0, (5, 7): 6.0, (5, 8): 3.0, (6, 7): 6.0, (6, 8): 3.0, (7, 8): 2.0, (7, 9): 8.0 }),
    (3, { (1, 2): 2.5, (1, 3): 2.5, (2, 4): 4.5, (3, 2): 1.0, (3, 4): 4.5, (4, 5): 4.0, (4, 6): 4.0 }),
  ]

  functions = [
    edge_betweenness1,
    edge_betweenness2,
  ]
  for function in functions:
    suite.addTests(EdgeBetweennessTest(inp, out, function) for inp, out in known_values)
  return suite


if __name__ == "__main__":
  # unittest.main()
  unittest.TextTestRunner().run(suite())