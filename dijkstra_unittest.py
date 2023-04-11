import unittest
from dijkstra import dijkstra
import networkx as nx
from load_custom_graph import load_custom_graph

class DijkstraTest(unittest.TestCase):
  def setUp(self):
    self.G1 = load_custom_graph(1)
    self.G2 = load_custom_graph(2)

  def test_dijkstra_G1_path_1_2(self):
    shortest_paths, distance = [ result[2] for result in dijkstra(self.G1, 1) ]
    self.assertEqual(shortest_paths, [[1,2]])
    self.assertEqual(distance, 1, 'Incorrect distance')
  
  def test_dijkstra_G1_path_1_4(self):
    shortest_paths, distance = [ result[4] for result in dijkstra(self.G1, 1) ]
    self.assertEqual(shortest_paths, [[1,5,4]])
    self.assertEqual(distance, 2, 'Incorrect distance')

  def test_dijkstra_G1_path_1_5(self):
    shortest_paths, distance = [ result[5] for result in dijkstra(self.G1, 1) ]
    self.assertEqual(shortest_paths, [[1,5]])
    self.assertEqual(distance, 1, 'Incorrect distance')

  def test_dijkstra_G1_path_2_6(self):
    shortest_paths, distance = [ result[6] for result in dijkstra(self.G1, 2) ]
    print(shortest_paths)
    self.assertCountEqual(shortest_paths, [[2,5,4,6], [2,3,4,6]])
    self.assertEqual(distance, 3, 'Incorrect distance')
  
  def test_dijkstra_G2_path_1_4(self):
    shortest_paths, distance = [ result[4] for result in dijkstra(self.G2, 1) ]
    self.assertEqual(shortest_paths, [[1,4]])
    self.assertEqual(distance, 1, 'Incorrect distance')
  
  def test_dijkstra_G2_path_1_7(self):
    shortest_paths, distance = [ result[7] for result in dijkstra(self.G2, 1) ]
    self.assertCountEqual(shortest_paths, [[1,4,5,7],[1,4,6,7]])
    self.assertEqual(distance, 3, 'Incorrect distance')

  def test_dijkstra_G2_path_1_9(self):
    shortest_paths, distance = [ result[9] for result in dijkstra(self.G2, 1) ]
    self.assertCountEqual(shortest_paths, [[1,4,5,7,9],[1,4,6,7,9]])
    self.assertEqual(distance, 4, 'Incorrect distance')

  def test_dijkstra_G2_path_2_8(self):
    shortest_paths, distance = [ result[8] for result in dijkstra(self.G2, 2) ]
    self.assertCountEqual(shortest_paths, [[2,3,4,6,8], [2,1,4,6,8], [2,3,4,5,8], [2,1,4,5,8]])
    self.assertEqual(distance, 4, 'Incorrect distance')

    
if __name__ == "__main__":
  unittest.main()