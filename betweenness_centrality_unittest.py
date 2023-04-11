import unittest
import networkx as nx
from betweenness_centrality import betweenness

class BetweennessCentralityTest(unittest.TestCase):
  def setUp(self) -> None:
    self.G = nx.Graph()
    self.G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)])
    return super().setUp()
  
  def test_betweenness(self):
    between = betweenness(self.G)
    self.assertDictEqual(between, {
      1: 0.0,
      2: 1.5,
      3: 1.0,
      4: 4.5,
      5: 3.0,
      6: 0.0
    })


if __name__ == "__main__":
  unittest.main()